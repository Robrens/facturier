# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet
from .models import Client, Product, Ligne, QuoteBill



# Create your views here.


class IndexView(ListView):
    model = Client

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return Client.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        else:
            return Client.objects.all()


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = "__all__"


    def get_success_url(self):
       return reverse("client-detail", args=[self.object.slug])


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = "__all__"

    def get_success_url(self):
        return reverse("client-detail", args=[self.object.slug])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('index')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"

    def get_success_url(self):
       return reverse("product-detail", args=[self.object.slug])


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse("product-detail", args=[self.object.slug])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('index')


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return Product.objects.filter(Q(name__icontains=query) | Q(slug__icontains=query))
        else:
            return Product.objects.all()


class ProductInline(InlineFormSet):
    model = Product


class LigneInline(InlineFormSet):
    model = Ligne
    fields = '__all__'


class CreateQuoteBillView(CreateWithInlinesView):
    model = QuoteBill
    inlines = [LigneInline,]
    fields = '__all__'

    def get_success_url(self):
        return reverse("quotebill-detail", args=[self.object.ref])


class UpdateQuoteBillView(UpdateWithInlinesView):
    model = QuoteBill
    inlines = [LigneInline,]
    fields = '__all__'


class QuoteBillListView(ListView):
    model = QuoteBill

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return QuoteBill.objects.filter(ref__icontains=query)
        else:
            return QuoteBill.objects.all()


class QuoteBillDetailView(DetailView):
    model=QuoteBill
