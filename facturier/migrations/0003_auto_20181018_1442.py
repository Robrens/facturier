# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0002_auto_20181018_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]