# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 23:31
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0009_remove_activity_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='body',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='{}'),
            preserve_default=False,
        ),
    ]
