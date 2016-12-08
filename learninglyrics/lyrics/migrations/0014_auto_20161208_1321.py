# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 17:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0013_auto_20161207_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 8, 17, 20, 58, 417230, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lyric',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 8, 17, 20, 58, 415956, tzinfo=utc)),
        ),
    ]