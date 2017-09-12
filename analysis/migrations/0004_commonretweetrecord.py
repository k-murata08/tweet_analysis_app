# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_commonfavoriterecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonRetweetRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('common_count', models.PositiveIntegerField()),
                ('text', models.CharField(max_length=200)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.Analysis')),
            ],
        ),
    ]