# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180727_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
