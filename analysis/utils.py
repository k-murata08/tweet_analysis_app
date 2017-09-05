# -*- coding: utf-8 -*-
from django.shortcuts import render

from accounts.models import TwitterAccount


def redirect_index(request):
    accounts = TwitterAccount.objects.all()

    return render(request, 'index.html', {
        'accounts': accounts
    })