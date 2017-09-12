# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from tweet_analysis import const as tc


class Profile(models.Model):
    ROLES = tc.USER_ROLE_CHOICES

    role = models.IntegerField(blank=False, choices=ROLES)
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)


class TwitterAccount(models.Model):
    twitter_id = models.CharField(blank=False, max_length=30)
    username = models.CharField(blank=False, max_length=30)
    image_url = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username

    @classmethod
    def create_account(cls, twitter_id, username, image_url):
        cls.objects.create(twitter_id=twitter_id, username=username, image_url=image_url)


class OathKey(models.Model):
    consumer_key = models.CharField(max_length=50, blank=False)
    consumer_secret = models.CharField(max_length=50, blank=False)
    access_token = models.CharField(max_length=50, blank=False)
    access_token_secret = models.CharField(max_length=50, blank=False)
    twitter_id = models.CharField(max_length=30, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_oath(cls, consumer_key, consumer_secret, access_token, access_token_secret, twitter_id):
        cls.objects.create(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            twitter_id=twitter_id
        )

    @classmethod
    def get_oath(cls):
        return cls.objects.latest('created_at')