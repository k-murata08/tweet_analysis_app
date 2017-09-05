# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import TwitterNameForm


def account_add(request):
    if request.method == 'POST':
        form = TwitterNameForm(request.POST)
        if form.is_valid():
            screen_name = form.cleaned_data['screen_name']
            print screen_name
            return redirect('account_confirm')
    else:
        form = TwitterNameForm()

    return render(request, 'account_form.html', {
        'form': form
    })


def account_confirm(request):
    return render(request, 'account_form_confirm.html')