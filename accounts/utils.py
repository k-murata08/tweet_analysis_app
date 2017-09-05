# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session

import json


def get_oath_session():
    """クエリを飛ばす時にしか使わない"""

    oath_key_dict = {
        "consumer_key": "lb26YD9K7h8JhNRFeGJlshWGX",
        "consumer_secret": "tcy6LZReXwELPtNBYk9MYz15w03kEJFdwmASdMaWRDzlQrhheV",
        "access_token": "1349624660-5fmFKCqnHaXTUMxyy9ESaCYYs65tZzXZqb5FWK3",
        "access_token_secret": "ifbZ4YwN2WIi6M8lpenyx2H9tWwWSFth3GMfU8K4AthTl"
    }

    oath = OAuth1Session(
        oath_key_dict["consumer_key"],
        oath_key_dict["consumer_secret"],
        oath_key_dict["access_token"],
        oath_key_dict["access_token_secret"]
    )
    return oath


def get_user_profile(screen_name):
    """15分間に900回回せる"""
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
