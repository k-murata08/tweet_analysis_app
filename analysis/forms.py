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
    common_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    follower_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )