# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160525_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=100),
        ),
    ]