# -*- coding: utf-8 -*-
from django import forms

import tweet_analysis.const as ta_const


class TwitterNameForm(forms.Form):
    screen_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
    ))


class OathForm(forms.Form):
    consumer_key = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
    ))
    consumer_secret = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
    ))
    access_token = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
    ))
    access_token_secret = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
    ))
    twitter_id = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
    ))


class UserForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password_confirm = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    role = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class':'flat'
            }
        ),
        choices=ta_const.USER_ROLE_CHOICES
    )
