# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20160528_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.CharField(blank=True, default='游客', max_length=100),
        ),
    ]
