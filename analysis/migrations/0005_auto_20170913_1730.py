# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_commonretweetrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='followers_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analysis',
            name='min_common_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
