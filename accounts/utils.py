# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session

import json

ANALYSYS_USER_ID = 740776275527237633


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


def get_user_profile():
    """15分間に900回回せる"""
    url = "https://api.twitter.com/1.1/users/show.json?"
    params = {
        "user_id": ANALYSYS_USER_ID,
        "include_entities": False
    }
    oath = get_oath_session()
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    profile = json.loads(responce.text, 'utf-8')
    return profile