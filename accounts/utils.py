# -*- coding: utf-8 -*-

from .models import OathKey

from requests_oauthlib import OAuth1Session
import json


def get_oath_session():
    """OathKeyのセッションを取得"""
    oath_key = OathKey.get_oath()
    oath = OAuth1Session(
        oath_key.consumer_key,
        oath_key.consumer_secret,
        oath_key.access_token,
        oath_key.access_token_secret
    )
    return oath


def fetch_result(url, params):
    oath = get_oath_session()
    response = oath.get(url, params=params)
    if response.status_code != 200:
        print "Error code: %d" % response.status_code
        raise ValueError
    result = json.loads(response.text, 'utf-8')
    return result


def get_user_profile(screen_name):
    """
    ユーザネームからプロフィールのjsonを取得
    15分間に900回回せる
    """
    url = "https://api.twitter.com/1.1/users/show.json?"
    params = {
        "screen_name": screen_name,
        "include_entities": False
    }
    return fetch_result(url, params)


def get_user_profiles(user_ids):
    """
    user_idのリストから、それらのプロフィールを取得
    15分間に900回回せる
    """
    url = "https://api.twitter.com/1.1/users/lookup.json?"
    params = {
        "user_id": user_ids,
        "include_entities": False
        }
    return fetch_result(url, params)


def get_user_timeline(user_id, tweets_count, include_rts):
    """
    ユーザIDからツイートを取得
    15分間に900回回せる
    """
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?"
    params = {
        "user_id": user_id,
        "trim_user": True,
        "count": tweets_count,
        "exclude_replies": True,
        "include_rts": include_rts
        }
    return fetch_result(url, params)


def get_favorite_tweets(user_id, count):
    """
    ユーザIDからファボツイートを取得
    15分間に75回回せる(1回200件が上限)
    """
    url = "https://api.twitter.com/1.1/favorites/list.json?"
    params = {
        "user_id": user_id,
        "count": count,
        "include_entities": False
    }
    return fetch_result(url, params)


def get_tweet(tweet_id):
    """
    ツイートの詳細を取得
    15分間に900回回せる
    """
    url = "https://api.twitter.com/1.1/statuses/show.json?"
    params = {
        "id": tweet_id,
        "include_my_retweet": False,
        "include_entities": False
    }
    return fetch_result(url, params)


def get_followers(user_id, users_count):
    """
    ユーザIDからフォロワーのjsonを取得
    15分間に15回回せる
    """
    url = "https://api.twitter.com/1.1/followers/list.json?"
    params = {
        "user_id": user_id,
        "count": users_count
        }
    followers = fetch_result(url, params)
    return followers['users']


def get_follower_ids(user_id, users_count, cursor):
    """
    ユーザIDからフォロワーのIDとcursorを取得
    15分間に15回回せる
    フォロワーidsとページングに使うnext_cursorが返る。次のページがないときにはnext_cursorは0で返る
    最初はcursorに-1を設定
    """
    url = "https://api.twitter.com/1.1/followers/ids.json?"
    params = {
        "user_id": user_id,
        "count": users_count,
        "cursor": cursor
        }
    follower_ids = fetch_result(url, params)
    return [follower_ids['ids'], follower_ids['next_cursor']]


def get_friends(user_id, users_count):
    """
    ユーザIDからフォローユーザのjsonを取得
    15分間に15回回せる
    user_idのユーザがフォローしているユーザ
    """
    url = "https://api.twitter.com/1.1/friends/list.json?"
    params = {
        "user_id": user_id,
        "count": users_count
        }
    friends = fetch_result(url, params)
    return friends['users']


def get_friend_ids(user_id, users_count, cursor):
    """
    ユーザIDからフォローユーザのIDとcursorを取得
    15分間に15回回せる
    """
    url = "https://api.twitter.com/1.1/friends/ids.json?"
    params = {
        "user_id": user_id,
        "count": users_count,
        "cursor": cursor
        }
    friend_ids = fetch_result(url, params)
    return [friend_ids['ids'], friend_ids['next_cursor']]
