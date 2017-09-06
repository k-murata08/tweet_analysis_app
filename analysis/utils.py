# -*- coding: utf-8 -*-
from django.shortcuts import render

from accounts.models import TwitterAccount, OathKey


def redirect_index(request):
    accounts = TwitterAccount.objects.all()
    oath_key = OathKey.get_oath()

    return render(request, 'index.html', {
        'accounts': accounts,
        'oath_key': oath_key
    })