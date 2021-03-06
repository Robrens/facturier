# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 14:30
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=200, populate_from='full_name', unique_with=['last_name'])),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.IntegerField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
                ('mail', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('price', models.IntegerField(max_length=20)),
                ('stock', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('transitions', models.BooleanField(default=False)),
                ('progress', models.CharField(choices=[('paid', 'paid'), ('in-progress', 'in-progress'), ('reflate', 'reflate')], default='in-progress', max_length=100)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.Client')),
            ],
        ),
        migrations.AddField(
            model_name='ligne',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.Product'),
        ),
        migrations.AddField(
            model_name='ligne',
            name='quoteBill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.QuoteBill'),
        ),
    ]
