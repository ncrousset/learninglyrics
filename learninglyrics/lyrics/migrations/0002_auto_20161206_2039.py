# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 00:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lyrics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lyric',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 7, 0, 39, 2, 736134, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='lyric',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]