"""facturier_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from facturier.views import IndexView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductListView, CreateQuoteBillView, UpdateQuoteBillView, QuoteBillListView, QuoteBillDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page="/")),
    
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^client/create/$', ClientCreateView.as_view(), name='client-create'),
    url(r'^client/(?P<slug>[-\w]+)/$', ClientDetailView.as_view(), name='client-detail'),
    url(r'^client/(?P<slug>[-\w]+)/edit/$', ClientUpdateView.as_view(), name='client-edit' ),
    url(r'^client/(?P<slug>[-\w]+)/delete/$', ClientDeleteView.as_view(), name='client-delete' ),

    url(r'^product/create/$', ProductCreateView.as_view(), name='product-create'),
    url(r'^product/list/$', ProductListView.as_view(), name='product-list'),
    url(r'^product/(?P<slug>[-\w]+)/$', ProductDetailView.as_view(), name='product-detail'),
    url(r'^product/(?P<slug>[-\w]+)/edit/$', ProductUpdateView.as_view(), name='product-edit' ),
    url(r'^product/(?P<slug>[-\w]+)/delete/$', ProductDeleteView.as_view(), name='product-delete' ),

    url(r'^quotebill/list/$', QuoteBillListView.as_view(), name='quotebill-list'),
    url(r'^quotebill/create/$', CreateQuoteBillView.as_view(), name='quotebill-create'),
    url(r'^quotebill/(?P<slug>[-\w]+)/$', QuoteBillDetailView.as_view(), name='quotebill-detail'),
    url(r'^quotebill/(?P<pk>\d+)/$', UpdateQuoteBillView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
