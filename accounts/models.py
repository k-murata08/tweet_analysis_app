# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    role = models.IntegerField(blank=False)
    user = models.OneToOneField(User)


class TwitterAccount(models.Model):
    twitter_id = models.CharField(blank=False)
    username = models.CharField(blank=False)
    image_url = models.URLField(blank=False)
