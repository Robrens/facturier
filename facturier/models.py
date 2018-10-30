# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


choices = []
for i in range(1, 3):
    choices.append((i, i))

status = [
    ('paid', 'paid'),
    ('in-progress', 'in-progress'),
    ('reflate', 'reflate'),
]



class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()

    class Meta:
       permissions = (
           ("read_product", "Can see product detail"),
       )

    def __unicode__(self):
        return self.slug


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='full_name', unique_with=[
                         'last_name'], max_length=200)
    address = models.CharField(max_length=300)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
       permissions = (
           ("read_client", "Can see the client detail"),
       )
        
    def __unicode__(self):
        return self.slug


    
class QuoteBill(models.Model):
    slug = models.SlugField(max_length=100)
    client = models.ForeignKey(Client, null=True, blank=True)
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de creation")
    is_bill = models.BooleanField(default=False)
    progress = models.CharField(choices=status, default='in-progress', max_length=100)

    class Meta:
       permissions = (
           ("read_client", "Can see the client detail"),
           ("send_quotebill", "Can send an email"),
       )
    def __unicode__(self):
        return self.slug


class Ligne(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, null=True, blank=True)
    quoteBill = models.ForeignKey(
        QuoteBill, null=True, blank=True)

    def multiply(self):
        return self.quantity * self.product.price
