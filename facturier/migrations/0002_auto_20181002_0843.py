# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-02 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=20)),
                ('id_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='devis_facture',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='devis_facture',
            name='quantity',
        ),
        migrations.AddField(
            model_name='devis_facture',
            name='id_ligne',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.Ligne'),
        ),
    ]
