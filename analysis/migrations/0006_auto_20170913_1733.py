# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_auto_20170913_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysis',
            old_name='followers_count',
            new_name='follower_count',
        ),
    ]
