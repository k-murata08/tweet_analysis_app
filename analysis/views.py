# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import utils as analysis_utils
from .forms import AnalysisAccountForm


@login_required
def index(request):
    return analysis_utils.redirect_index(request)


def common_follow_form(request):
    if request.method == 'POST':
        form = AnalysisAccountForm(request.POST)
        if form.is_valid():
            print "aaa"
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
