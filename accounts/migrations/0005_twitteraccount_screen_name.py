# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170906_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteraccount',
            name='screen_name',
            field=models.CharField(default='aaa', max_length=30),
            preserve_default=False,
        ),
    ]