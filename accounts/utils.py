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
    oath = get_oath_session()
    response = oath.get(url, params=params)
    if response.status_code != 200:
        print "Error code: %d" % response.status_code
        raise ValueError
    profile = json.loads(response.text, 'utf-8')
    return profile
