# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.models import OathKey, TwitterAccount


class OathKeyAdmin(admin.ModelAdmin):
    list_display = ('consumer_key', 'consumer_secret', 'access_token', 'access_token_secret', 'twitter_id', 'created_at')


class TwitterAccountAdmin(admin.ModelAdmin):
    list_display = ('twitter_id', 'username', 'image_url', 'created_at')


admin.site.register(OathKey, OathKeyAdmin)
admin.site.register(TwitterAccount, TwitterAccountAdmin)

