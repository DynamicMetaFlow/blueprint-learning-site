# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-25 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0027_auto_20170716_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='summary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]