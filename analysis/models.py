# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Analysis(models.Model):
    account = models.ForeignKey('accounts.TwitterAccount')
    user = models.ForeignKey(User)
    follower_count = models.PositiveIntegerField(blank=False)
    min_common_count = models.PositiveIntegerField(blank=False)
    category = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, account, user, follower_count, min_common_count, category):
        return cls.objects.create(
            account=account,
            user=user,
            follower_count=follower_count,
            min_common_count=min_common_count,
            category=category
        )


class CommonFollowRecord(models.Model):
    twitter_id = models.CharField(blank=False, max_length=30)
    username = models.CharField(blank=False, max_length=30)
    common_count = models.PositiveIntegerField(blank=False)
    followers_count = models.PositiveIntegerField(blank=False)
    follow_rate = models.FloatField(blank=False)
    follower_ratio = models.FloatField(blank=False)
    factor = models.FloatField(blank=False)
    analysis = models.ForeignKey('Analysis')

    @classmethod
    def create(cls, twitter_id, username, common_count, followers_count, follow_rate, follow_ratio, factor, analysis):
        return cls.objects.create(
            twitter_id=twitter_id,
            username=username,
            common_count=common_count,
            followers_count=followers_count,
            follow_rate=follow_rate,
            follow_ratio=follow_ratio,
            factor=factor,
            analysis=analysis
        )


class CommonFavoriteRecord(models.Model):
    tweet_id = models.CharField(blank=False, max_length=30)
    username = models.CharField(blank=False, max_length=30)
    common_count = models.PositiveIntegerField(blank=False)
    text = models.CharField(blank=False, max_length=200)
    analysis = models.ForeignKey('Analysis')

    @classmethod
    def create(cls, tweet_id, username, common_count, text, analysis):
        return cls.objects.create(
            tweet_id=tweet_id,
            username=username,
            common_count=common_count,
            text=text,
            analysis=analysis
        )


class CommonRetweetRecord(models.Model):
    tweet_id = models.CharField(blank=False, max_length=30)
    username = models.CharField(blank=False, max_length=30)
    common_count = models.PositiveIntegerField(blank=False)
    text = models.CharField(blank=False, max_length=200)
    analysis = models.ForeignKey('Analysis')

    @classmethod
    def create(cls, tweet_id, username, common_count, text, analysis):
        return cls.objects.create(
            tweet_id=tweet_id,
            username=username,
            common_count=common_count,
            text=text,
            analysis=analysis
        )