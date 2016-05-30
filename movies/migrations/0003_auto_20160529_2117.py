# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20160525_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_director',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_stars',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_writers',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_content',
            field=models.TextField(),
        ),
    ]
