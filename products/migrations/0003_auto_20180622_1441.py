# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='available_stock',
        ),
    ]