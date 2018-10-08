# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Client, Product, Ligne, QuoteBill

# Register your models here.
class LigneAdmin(admin.StackedInline):
    model = Ligne

class QuoteBillAdmin(admin.ModelAdmin):
    list_display=('client',)
    inlines=[LigneAdmin,]


admin.site.register(QuoteBill, QuoteBillAdmin)

admin.site.register(Client)


admin.site.register(Product)