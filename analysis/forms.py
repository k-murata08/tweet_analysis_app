# -*- coding: utf-8 -*-
from django import forms

from accounts.models import TwitterAccount


class AnalysisAccountForm(forms.Form):
    accounts = forms.ModelChoiceField(
        queryset=TwitterAccount.objects.all(),
        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        )
    )