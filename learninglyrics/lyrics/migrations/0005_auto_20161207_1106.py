# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 15:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0004_auto_20161207_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Title')),
                ('url_cover_page', models.URLField(max_length=100, null=True)),
                ('published', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 7, 15, 6, 52, 920399, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lyric',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 7, 15, 6, 52, 919376, tzinfo=utc)),
        ),
    ]
