# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

import utils as analysis_utils


@login_required
def index(request):
    return analysis_utils.redirect_index(request)