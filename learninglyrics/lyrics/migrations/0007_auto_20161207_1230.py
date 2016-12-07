# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 16:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0006_auto_20161207_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 7, 16, 30, 34, 876476, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lyric',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 7, 16, 30, 34, 875398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='url_pronunciation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
