# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .forms import TwitterNameForm, OathForm, UserForm
from .models import TwitterAccount, OathKey, Profile
import utils as account_utils
import analysis.utils as analysis_utils


def logout_to_index(request):
    logout(request)
    return redirect('index')


def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            user = User.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            Profile.objects.create(
                role=form.cleaned_data['role'],
                user=user
            )
            return analysis_utils.redirect_index(request)

    else:
        form = UserForm()

    return render(request, 'user_form.html', {
        'form': form
    })


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
        return analysis_utils.redirect_index(request)

    else:
        try:
            context = {
                'twitter_id': profile['id'],
                'name': profile['name'],
                'image_url': profile['profile_image_url']
            }
            return render(request, 'account_form_confirm.html', context)

        except ValueError:
            return analysis_utils.redirect_index(request)


def oath_add(request):
    if request.method == 'POST':
        form = OathForm(request.POST)
        if form.is_valid():
            OathKey.create_oath(
                form.cleaned_data['consumer_key'],
                form.cleaned_data['consumer_secret'],
                form.cleaned_data['access_token'],
                form.cleaned_data['access_token_secret'],
                form.cleaned_data['twitter_id']
            )
            return analysis_utils.redirect_index(request)
    else:
        form = OathForm

    return render(request, 'oauth_form.html', {
        'form': form
    })