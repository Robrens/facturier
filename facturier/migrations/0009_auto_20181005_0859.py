# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0008_auto_20181005_0730'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('price', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='quote_bill',
            name='id_client',
        ),
        migrations.RemoveField(
            model_name='quote_bill',
            name='id_ligne',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='ligne',
            old_name='id_product',
            new_name='product',
        ),
        migrations.DeleteModel(
            name='Quote_Bill',
        ),
        migrations.AddField(
            model_name='quotebill',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.Client'),
        ),
        migrations.AddField(
            model_name='ligne',
            name='quoteBill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.QuoteBill'),
        ),
    ]