# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from tweet_analysis import const as tc


class Profile(models.Model):
    ROLES = tc.USER_ROLES

    role = models.IntegerField(blank=False, choices=ROLES)
    user = models.OneToOneField(User)


class TwitterAccount(models.Model):
    twitter_id = models.CharField(blank=False, max_length=30)
    username = models.CharField(blank=False, max_length=30)
    image_url = models.URLField(blank=False)
