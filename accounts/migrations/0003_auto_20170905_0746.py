# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_oauthkey'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OauthKey',
            new_name='OathKey',
        ),
    ]
