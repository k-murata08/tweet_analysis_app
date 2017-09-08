# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import transaction

import utils as analysis_utils
from .forms import AnalysisAccountForm
from accounts.models import TwitterAccount


@login_required
def index(request):
    return analysis_utils.redirect_index(request)


@transaction.atomic
def common_follow_form(request):
    if request.method == 'POST':
        form = AnalysisAccountForm(request.POST)
        if form.is_valid():
            account = TwitterAccount.objects.get(id=request.POST['accounts'])

            analysis_utils.analysis_follower_friends(request.user, account)
            return analysis_utils.redirect_index(request)

    else:
        form = AnalysisAccountForm()

    return render(request, 'common_follow_form.html', {
        'form': form
    })


def common_fav_form(request):
    if request.method == 'POST':
        form = AnalysisAccountForm(request.POST)
        if form.is_valid():
            print "aaa"
            return analysis_utils.redirect_index(request)

    else:
        form = AnalysisAccountForm()

    return render(request, 'common_fav_form.html', {
        'form': form
    })


def common_rt_form(request):
    if request.method == 'POST':
        form = AnalysisAccountForm(request.POST)
        if form.is_valid():
            print "aaa"
            return analysis_utils.redirect_index(request)

    else:
        form = AnalysisAccountForm()

    return render(request, 'common_rt_form.html', {
        'form': form
    })
