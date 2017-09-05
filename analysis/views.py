# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from accounts.models import TwitterAccount
import utils as analysis_utils


def index(request):
    return analysis_utils.redirect_index(request)