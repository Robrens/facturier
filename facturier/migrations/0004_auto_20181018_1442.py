# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0003_auto_20181018_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ligne',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
