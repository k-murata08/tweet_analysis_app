# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User

from accounts.models import TwitterAccount, OathKey


def redirect_index(request):
    accounts = TwitterAccount.objects.all()
    oath_key = OathKey.get_oath()
    users = User.objects.all()

    return render(request, 'index.html', {
        'accounts': accounts,
        'oath_key': oath_key,
        'users': users,
    })