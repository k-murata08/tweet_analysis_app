# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import TwitterNameForm, OathForm
from .models import TwitterAccount
import utils as account_utils


def account_add(request):
    if request.method == 'POST':
        form = TwitterNameForm(request.POST)
        if form.is_valid():
            screen_name = form.cleaned_data['screen_name']
            return redirect('account_confirm', screen_name=screen_name)
    else:
        form = TwitterNameForm()

    return render(request, 'account_form.html', {
        'form': form
    })


def account_confirm(request, screen_name):
    profile = account_utils.get_user_profile(screen_name)
    if request.method == 'POST':
        TwitterAccount.create_account(profile['id'], profile['name'], profile['profile_image_url'])
        return redirect('index')

    else:
        try:
            context = {
                'twitter_id': profile['id'],
                'name': profile['name'],
                'image_url': profile['profile_image_url']
            }
            return render(request, 'account_form_confirm.html', context)

        except ValueError:
            return redirect('account_add')


def oath_add(request):
    if request.method == 'POST':
        form = OathForm(request.POST)
        if form.is_valid():
            print "aiueo"
            return redirect('index')
    else:
        form = OathForm

    return render(request, 'oauth_form.html', {
        'form': form
    })