# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField(max_length=20)
    stock = models.IntegerField(max_length=20)

    def __unicode__(self):
        return self.slug


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='full_name', unique_with=[
                         'last_name'], max_length=200)
    address = models.CharField(max_length=300)
    zip_code = models.IntegerField(max_length=20)
    city = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=20)
    mail = models.EmailField(max_length=50)

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

        
    def __unicode__(self):
        return self.slug


class QuoteBill(models.Model):
    ref = models.SlugField(max_length=100)
    client = models.ForeignKey(Client, null=True, blank=True)
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de creation")


class Ligne(models.Model):
    quantity = models.IntegerField(max_length=20)
    product = models.ForeignKey(Product, null=True, blank=True)
    quoteBill = models.ForeignKey(
        QuoteBill, null=True, blank=True)
