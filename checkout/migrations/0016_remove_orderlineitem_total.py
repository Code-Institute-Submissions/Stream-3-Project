# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0015_auto_20180712_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='total',
        ),
    ]
