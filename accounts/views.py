# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def account_add(request):
    return render(request, 'account_form.html')
