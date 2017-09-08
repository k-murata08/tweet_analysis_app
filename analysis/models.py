# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Analysis(models.Model):
    account = models.ForeignKey('accounts.TwitterAccount')
    user = models.ForeignKey(User)
    category = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class CommonFollowRecord(models.Model):
    twitter_id = models.CharField(blank=False, max_length=30)
    username = models.CharField(blank=False, max_length=30)
    common_count = models.PositiveIntegerField(blank=False)
    followers_count = models.PositiveIntegerField(blank=False)
    follow_rate = models.FloatField(blank=False)
    follow_ratio = models.FloatField(blank=False)
    factor = models.FloatField(blank=False)
    analysis = models.ForeignKey('Analysis')