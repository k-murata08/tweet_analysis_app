# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from accounts.models import TwitterAccount


def index(request):
    accounts = TwitterAccount.objects.all()

    return render(request, 'index.html', {
        'accounts': accounts
    })
