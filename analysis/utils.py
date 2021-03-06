# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import connection

from accounts.models import TwitterAccount, OathKey
from .models import Analysis, CommonFollowRecord, CommonFavoriteRecord, CommonRetweetRecord
import accounts.utils as ac_utils
import tweet_analysis.const as ta_const

from time import sleep
from datetime import datetime as dt
import collections
import traceback
from background_task import background


def redirect_index(request):
    accounts = TwitterAccount.objects.all()
    try:
        oath_key = OathKey.get_oath()
    except ObjectDoesNotExist:
        oath_key = None
    users = User.objects.all()

    tasks = get_background_tasks()

    return render(request, 'index.html', {
        'accounts': accounts,
        'oath_key': oath_key,
        'users': users,
        'tasks': tasks
    })


def get_background_tasks():
    # 実行中のバックグラウンド処理を取得
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM background_task")
    rows = cursor.fetchall()

    tasks = []
    for row in rows:
        tasks.append({
            'name': row[9],
            'run_at': row[6],
            'task_params': row[2]
        })

    return tasks


# --------------- 分析用関数 ----------------------


class TwUser:
    """
    ツイッターのユーザクラス
    一部のアカウント情報を保持しておくために使用
    """
    def __init__(self, id, name, description, friends_count, created_at, is_protected):
        self.id = id
        self.name = name
        self.description = description
        self.friends_count = friends_count
        self.created_at = created_at
        self.is_protected = is_protected


def print_step_log(step_name, index, list_len):
    print step_name + " " + str(index+1) + "/" + str(list_len)


def split_list(_list, n):
    """listをn個ずつの要素を持ったリストに分割する(余は余りでリストになる)"""
    return [_list[x:x+n] for x in range(0, len(_list), n)]


def get_follower_ids(user_id):
    """
    フォロワーの全IDリストを返す
    """
    follower_ids = []
    cursor = -1

    # 一回のフォロワーID取得上限が5000件なので、5000件以上あればループs
    for i in range(10):
        print "CreateFollowerIDs"
        try:
            f_ids_cursor = ac_utils.get_follower_ids(user_id, 5000, cursor)
        except ValueError:
            traceback.print_exc()
            break

        if f_ids_cursor is None or f_ids_cursor == []:
            break

        follower_ids.extend(f_ids_cursor[0])
        if f_ids_cursor[1] == 0: # 全てのfollower_idsを取得したらbreak
            break
        cursor = f_ids_cursor[1]
        sleep(1)

    return follower_ids


def create_users_from_ids(user_ids):
    """
    ツイッターユーザIDリストからTwUserのオブジェクトリストを返す
    """
    users = []
    user_ids_list = split_list(user_ids, 100)
    for index, ids in enumerate(user_ids_list):
        print_step_log("CreateUsersList", index, len(user_ids_list))
        try:
            profs = ac_utils.get_user_profiles(ids)
        except ValueError:
            traceback.print_exc()
            sleep(1)
            continue

        if profs is None or profs == []:
            continue

        for prof in profs:
            user = TwUser(
                id=prof['id'],
                name=prof['name'],
                description=prof['description'],
                friends_count=prof['friends_count'],
                created_at=dt.strptime(prof['created_at'], "%a %b %d %H:%M:%S +0000 %Y"),
                is_protected=prof['protected']
            )
            users.append(user)
        sleep(1)

    return users


def create_friend_ids_from_users(users):
    """
    TwUsersたちのフォロイーのID(重複可)のリストを生成
    """
    friend_ids = []

    for index, user in enumerate(users):
        print_step_log("CreateFriendID", index, len(users))
        cursor = -1
        # 一回のフォロイーID取得上限が5000件なので、5000件以上あればループ
        for i in range(10):
            try:
                ids_cursor = ac_utils.get_friend_ids(user.id, 5000, cursor)
            except ValueError:
                traceback.print_exc()
                sleep(60)
                break

            if ids_cursor is None or ids_cursor == []:
                sleep(60)
                break

            friend_ids.extend(ids_cursor[0])
            cursor = ids_cursor[1]

            if cursor == 0:
                sleep(60)
                break
            print "Friend count over 5000 creating..."
            sleep(60)

    return friend_ids


def get_favorites_from_users(users):
    """
    Userオブジェクトリストから
    そのユーザのファボツイート(200件/人)を返す
    """
    favorite_tweet_ids = []
    for index, user in enumerate(users):
        print_step_log("CreateFavoritesList", index, len(users))
        try:
            favs = ac_utils.get_favorite_tweets(user.id, 200)
        except ValueError:
            traceback.print_exc()
            sleep(12)
            continue

        if favs is None or favs == []:
            sleep(12)
            continue

        for fav in favs:
            favorite_tweet_ids.append(fav['id'])
        sleep(12)

    return favorite_tweet_ids


# ----- 分析関数 ---------
@background(queue='common_follow')
def analysis_follower_friends(request_user_id, account_id, common_count, follower_count):
    """
    フォロワーの中でVALID_USER_MAX_CREATED_AT年以前の登録ユーザをフォロー数の降順に並べて
    分析したアカウントをFriendオブジェクトにしてリストで返す
    """
    request_user = User.objects.get(id=request_user_id)
    account = TwitterAccount.objects.get(id=account_id)

    analysis_record = Analysis.create(
        account=account,
        user=request_user,
        category=ta_const.ANALYSIS_CATEGORY['common_follow'],
        follower_count=follower_count,
        min_common_count=common_count,
    )

    follower_ids = get_follower_ids(user_id=account.twitter_id)
    followers = create_users_from_ids(user_ids=follower_ids)

    # VALID_USER_MAX_CREATED_AT年以前のユーザで絞り込み,
    # 非公開アカウントを弾き,
    # フォロー数の多い順で並べる
    followers = filter(lambda obj: obj.created_at.year <= 2016, followers)
    followers = filter(lambda obj: obj.is_protected is False, followers)
    followers = sorted(followers, key=lambda obj: obj.friends_count, reverse=True)

    followers = followers[0:int(follower_count)]

    # フォロワーがフォローしている人
    friend_ids = create_friend_ids_from_users(users=followers)

    # フォロイーのIDをキーにして、フォロイーが何人にフォローされているかを格納
    friends_counter_dict = collections.Counter(friend_ids)

    # 自分をFriendオブジェクトに登録するのは係数計算の部分で情報が必要なため
    my_prof = ac_utils.get_user_profile_from_id(account.twitter_id)
    my_count = friends_counter_dict[account.twitter_id]
    my_followers_count = my_prof['followers_count']
    sleep(1)

    # フレンドのクラスの配列を作る
    step = 0
    for key, value in friends_counter_dict.items():
        step += 1
        print_step_log("CreateFriendList", step, len(friends_counter_dict))
        # 何人以上のアカウントをとってくるか
        if value < int(common_count):
            continue

        try:
            prof = ac_utils.get_user_profile_from_id(key)
        except ValueError:
            traceback.print_exc()
            sleep(1)
            continue

        if prof is None or prof == []:
            sleep(1)
            continue

        # フォロー率、フォロー比、係数を計算
        if my_count != 0:
            follow_rate = float(value) / float(my_count)
        else:
            follow_rate = 0

        if my_followers_count != 0:
            follow_ratio = float(prof['followers_count']) / float(my_followers_count)
        else:
            follow_ratio = 0

        if follow_ratio != 0:
            factor = follow_rate / follow_ratio * 1000
        else:
            factor = 0

        CommonFollowRecord.create(
            twitter_id=key,
            username=prof['name'],
            common_count=value,
            followers_count=prof['followers_count'],
            follow_rate=round(follow_rate * 100, 2),
            follow_ratio=round(follow_ratio, 1),
            factor=round(factor, 1),
            analysis=analysis_record
        )
        sleep(1)


@background(queue='common_fav')
def analysis_follower_favorite(request_user_id, account_id, common_count, follower_count):
    """
    フォロワーの共通ファボ分析
    """
    request_user = User.objects.get(id=request_user_id)
    account = TwitterAccount.objects.get(id=account_id)

    analysis_record = Analysis.create(
        account=account,
        user=request_user,
        follower_count=follower_count,
        min_common_count=common_count,
        category=ta_const.ANALYSIS_CATEGORY['common_fav']
    )
    follower_ids = get_follower_ids(user_id=account.twitter_id)
    followers = create_users_from_ids(user_ids=follower_ids)

    followers = filter(lambda obj: obj.created_at.year <= 2016, followers)
    followers = filter(lambda obj: obj.is_protected is False, followers)
    followers = sorted(followers, key=lambda obj: obj.friends_count, reverse=False)
    followers = followers[0:int(follower_count)]

    favorites = get_favorites_from_users(followers)

    # ファボツイートのIDをキーにして、ファボツイートが何人にファボされているかを格納
    favorites_counter_dict = collections.Counter(favorites)

    step = 0
    for key, value in favorites_counter_dict.items():
        print_step_log("GetFavorites", step, len(favorites_counter_dict))
        step += 1
        if value < int(common_count):
            continue

        try:
            tweet = ac_utils.get_tweet(key)
        except ValueError:
            traceback.print_exc()
            sleep(1)
            continue

        if tweet is None or tweet == []:
            sleep(1)
            continue

        CommonFavoriteRecord.create(
            tweet_id=key,
            username=tweet['user']['name'],
            common_count=value,
            text=tweet['text'],
            analysis=analysis_record
        )
        sleep(1)


@background(queue='common_rt')
def analysis_follower_retweet(request_user_id, account_id, common_count, follower_count):
    """
    共通リツイート分析
    """
    request_user = User.objects.get(id=request_user_id)
    account = TwitterAccount.objects.get(id=account_id)

    analysis_record = Analysis.create(
        account=account,
        user=request_user,
        follower_count=follower_count,
        min_common_count=common_count,
        category=ta_const.ANALYSIS_CATEGORY['common_rt']
    )
    follower_ids = get_follower_ids(user_id=account.twitter_id)
    followers = create_users_from_ids(user_ids=follower_ids)

    followers = filter(lambda obj:obj.created_at.year <= 2016 , followers)
    followers = filter(lambda obj:obj.is_protected is False, followers)
    followers = sorted(followers, key=lambda obj: obj.friends_count, reverse=False)
    followers = followers[0:int(follower_count)]

    retweet_ids = []
    for index, follower in enumerate(followers):
        print_step_log("CreateRetweetList", index, len(followers))
        try:
            follower_tweets = ac_utils.get_user_timeline(user_id=follower.id, tweets_count=200, include_rts=True)
            follower_retweets = filter(lambda obj: obj.has_key("retweeted_status"), follower_tweets)
            retweet_tweets = [retweet["retweeted_status"] for retweet in follower_retweets]
        except ValueError:
            traceback.print_exc()
            sleep(1)
            continue

        if retweet_tweets is None or retweet_tweets == []:
            sleep(1)
            continue

        ids = [retweet['id'] for retweet in retweet_tweets]
        retweet_ids.extend(ids)
        sleep(1)

    retweet_counter_dict = collections.Counter(retweet_ids)

    step = 0
    for key, value in retweet_counter_dict.items():
        print_step_log("GetTweet", step, len(retweet_counter_dict))
        step += 1
        if value < int(common_count):
            continue

        try:
            tweet = ac_utils.get_tweet(key)
        except ValueError:
            traceback.print_exc()
            sleep(1)
            continue

        if tweet is None or tweet == []:
            sleep(1)
            continue

        CommonRetweetRecord.create(
            tweet_id=key,
            username=tweet['user']['name'],
            common_count=value,
            text=tweet['text'],
            analysis=analysis_record
        )
        sleep(1)