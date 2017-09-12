# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import utils as analysis_utils
from .forms import AnalysisAccountForm
from accounts.models import TwitterAccount
from .models import Analysis, CommonFollowRecord
import tweet_analysis.const as ta_const


@login_required
def index(request):
    return analysis_utils.redirect_index(request)


def common_follow_form(request):
    if request.method == 'POST':
        form = AnalysisAccountForm(request.POST)
        if form.is_valid():
            account = TwitterAccount.objects.get(id=request.POST['accounts'])

            analysis_utils.analysis_follower_friends(request.user, account, request.POST['common_count'], request.POST['follower_count'])
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
            account = TwitterAccount.objects.get(id=request.POST['accounts'])

            analysis_utils.analysis_follower_favorite(request.user, account, request.POST['common_count'], request.POST['follower_count'])
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


def common_follow_result(request):
    analysis = Analysis.objects.filter(
        category=ta_const.ANALYSIS_CATEGORY['common_follow']
    ).order_by('-created_at')

    return render(request, 'result.html', {
        'analysis': analysis,
        'title': "共通フォロー分析"
    })


def common_follow_result_detail(request, pk):
    analysis = Analysis.objects.get(id=pk)
    records = CommonFollowRecord.objects.filter(analysis=analysis).order_by('-common_count')
    return render(request, 'common_follow_result_detail.html', {
        'records': records,
        'analysis': analysis
    })