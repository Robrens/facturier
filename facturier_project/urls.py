"""facturier_project URL Configuration"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from facturier.views import IndexView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView
from facturier.views import ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductListView
from facturier.views import CreateQuoteBillView, UpdateQuoteBillView, QuoteBillListView, QuoteBillDetailView, UpdateQuoteBillProductView, QuoteBillPrintView
from facturier.views import DeleteLineView, CreateLineView, EmailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page="/")),
    
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^client/create/$', ClientCreateView.as_view(), name='client-create'),
    url(r'^client/(?P<slug>[-\w]+)/$', ClientDetailView.as_view(), name='client-detail'),
    url(r'^client/(?P<slug>[-\w]+)/edit/e$', ClientUpdateView.as_view(), name='client-edit' ),
    url(r'^client/(?P<slug>[-\w]+)/delete/$', ClientDeleteView.as_view(), name='client-delete' ),

    url(r'^product/create/$', ProductCreateView.as_view(), name='product-create'),
    url(r'^product/list/$', ProductListView.as_view(), name='product-list'),
    url(r'^product/(?P<slug>[-\w]+)/$', ProductDetailView.as_view(), name='product-detail'),
    url(r'^product/(?P<slug>[-\w]+)/edit/$', ProductUpdateView.as_view(), name='product-edit' ),
    url(r'^product/(?P<slug>[-\w]+)/delete/$', ProductDeleteView.as_view(), name='product-delete' ),
    url(r'^product/(?P<slug>[-\w]+)/(?P<field_name>[-\w]+)/edit/$', UpdateQuoteBillProductView.as_view(), name='product-quotebill-edit'),

    url(r'^ligne/delete/$', DeleteLineView.as_view(), name='line-quotebill-delete'),
    url(r'^ligne/add/$', CreateLineView.as_view(), name='line-quotebill-add'),



    url(r'^quotebill/create/$', CreateQuoteBillView.as_view(), name='quotebill-create'),
    url(r'^quotebill/list/$', QuoteBillListView.as_view(), name='quotebill-list'),
    url(r'^quotebill/(?P<slug>[-\w]+)/$', QuoteBillDetailView.as_view(), name='quotebill-detail'),
    url(r'^quotebill/(?P<slug>[-\w]+)/pdf/$',
        QuoteBillPrintView.as_view(), name='quotebill-detail-pdf'),
    url(r'^quotebill/(?P<slug>[-\w]+)/email/$', EmailView.as_view(), name='quotebill-email'),
    url(r'^quotebill/(?P<slug>[-\w]+)/(?P<field_name>[-\w]+)/edit/$', UpdateQuoteBillView.as_view(), name='quotebill-edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
