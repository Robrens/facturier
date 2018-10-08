# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 09:35
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0014_auto_20181005_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=200, populate_from=('first_name', 'last_name')),
        ),
    ]
