# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 17:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0008_auto_20161207_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorsHasProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 7, 17, 49, 31, 978801, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lyric',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 7, 17, 49, 31, 977805, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='authorshasproduction',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lyrics.Author'),
        ),
        migrations.AddField(
            model_name='authorshasproduction',
            name='production',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lyrics.MusicProduction'),
        ),
        migrations.AlterUniqueTogether(
            name='authorshasproduction',
            unique_together=set([('author', 'production')]),
        ),
    ]