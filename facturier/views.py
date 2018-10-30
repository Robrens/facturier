# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DeleteView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet
from django_weasyprint import WeasyTemplateResponseMixin
from .models import Client, Product, Ligne, QuoteBill, status
from .forms import QuotationFormLine
import weasyprint

class IndexView(ListView):
    model = Client

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return Client.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        else:
            return Client.objects.all()


class ClientDetailView(PermissionRequiredMixin, DetailView):
    model = Client
    permission_required = 'facturier.read_client'


class ClientCreateView(PermissionRequiredMixin, CreateView):
    model = Client
    permission_required = 'facturier.add_client'

    fields = "__all__"


    def get_success_url(self):
       return reverse("client-detail", args=[self.object.slug])


class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    model = Client
    permission_required = 'facturier.change_client'
    fields = "__all__"

    def get_success_url(self):
        return reverse("client-detail", args=[self.object.slug])


class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    model = Client
    permission_required = 'facturier.delete_client'
    success_url = reverse_lazy('index')


# //////////////////-----------PRODUCT-----------////////////////////////


class ProductDetailView(PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'facturier.read_product'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    permission_required = 'facturier.add_product'
    fields = "__all__"

    def get_success_url(self):
       return reverse("product-detail", args=[self.object.slug])


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = 'facturier.change_product'

    fields = "__all__"

    def get_success_url(self):
        return reverse("product-detail", args=[self.object.slug])


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'facturier.delete_product'
    success_url = reverse_lazy('index')


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return Product.objects.filter(Q(name__icontains=query) | Q(slug__icontains=query))
        else:
            return Product.objects.all()


class ProductInline(PermissionRequiredMixin, InlineFormSet):
    model = Product
    permission_required = 'facturier.transfert_product'



class LigneInline(PermissionRequiredMixin, InlineFormSet):
    model = Ligne
    permission_required = 'facturier.transfert_product'

    fields = '__all__'


# //////////////////-----------QUOTE-BILL-----------////////////////////////


class CreateQuoteBillView(PermissionRequiredMixin, CreateWithInlinesView):
    model = QuoteBill
    permission_required = 'facturier.add_quotebill'
    inlines = [LigneInline,]
    fields = '__all__'

    def get_success_url(self):
        return reverse("quotebill-detail", args=[self.object.slug])


class QuoteBillListView(ListView):
    model = QuoteBill

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context["progress"] = status
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        result = self.request.GET.get('d', None)
        if query != None:
            if result != None:
                return QuoteBill.objects.filter(slug__icontains=query, progress__icontains=result)
            return QuoteBill.objects.filter(slug__icontains=query)
        else:
            if result != None:
                return QuoteBill.objects.filter(progress__icontains=result)
            return QuoteBill.objects.all()


class QuoteBillDetailView(PermissionRequiredMixin, DetailView):
    model = QuoteBill
    permission_required = 'facturier.read_quotebill'


    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['ligne'] = Ligne.objects.all()
        context['product'] = Product.objects.all()
        context['formline'] = QuotationFormLine
        return context


class QuoteBillPrintView(WeasyTemplateResponseMixin, QuoteBillDetailView):

    # output of DetailView rendered as PDF
    def get_context_data(self, **kwargs):
        context = QuoteBillDetailView.get_context_data(self, **kwargs)
        context["is_pdf"] = True
        return context


@method_decorator(csrf_exempt, name='dispatch')
class UpdateQuoteBillView(PermissionRequiredMixin, View):
    permission_required = 'facturier.change_quotebill'

    def post(self, request, slug, field_name, **kwargs):
        quotebill = QuoteBill.objects.get(slug=slug)
        setattr(quotebill, field_name, request.POST.get("value"))
        quotebill.save()
        return HttpResponse({'success': True})

@method_decorator(csrf_exempt, name='dispatch')
class UpdateQuoteBillProductView(PermissionRequiredMixin, View):
    permission_required = 'facturier.change_quotebill'

    def post(self, request, slug, field_name, **kwargs):
        product = Product.objects.get(slug=slug)
        setattr(product, field_name, request.POST.get("value"))
        product.save()
        return HttpResponse({'success': True})


@method_decorator(csrf_exempt, name='dispatch')
class DeleteLineView(PermissionRequiredMixin, View):
    permission_required = 'facturier.delete_quotebill'

    def post(self, request, **kwargs):
        ligne = Ligne.objects.get(pk=request.POST.get('pk'))
        ligne.delete()
        return HttpResponse({'success': True})


@method_decorator(csrf_exempt, name='dispatch')
class CreateLineView(PermissionRequiredMixin, CreateView):
    model = Ligne
    permission_required = 'facturier.add_quotebill'
    form_class = QuotationFormLine

    def get_success_url(self):
        return reverse("quotebill-detail", args=[self.object.quoteBill.slug])


class EmailView(PermissionRequiredMixin, View):
    permission_required = 'facturier.send_quotebill'

    def get(self, request, slug, **kwargs):

        quotebill = QuoteBill.objects.get(slug=slug)
        client_email = quotebill.client.email

        html = render_to_string('facturier/quotebill_detail.html', {"quotebill": quotebill, "is_pdf" : True})
        url = reverse("quotebill-detail", args=[quotebill.slug])
        pdf = weasyprint.HTML(string=html, base_url=url).write_pdf()
        from_email = 'azerty@gmail.com'
        to_emails = [client_email]
        subject = "Your bill"
        message = 'plop'
        email = EmailMessage(subject, body=message, from_email=from_email, to=to_emails)
        email.attach("devis.pdf", pdf, "application/pdf")
        email.content_subtype = "pdf"  # Main content is now text/html
        email.send()
        return HttpResponse({"success": True})

