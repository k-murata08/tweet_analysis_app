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
    access_key = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
    ))
    access_key_secret = forms.CharField(
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