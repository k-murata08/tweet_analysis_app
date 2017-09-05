# -*- coding: utf-8 -*-
from django import forms


class TwitterNameForm(forms.Form):
    screen_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))