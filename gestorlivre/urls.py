"""gestorlivre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import clientes.views, comercial.views, estoque.views, financeiro.views, fornecedores.views, rh.views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^clientes/', clientes.views.clientes),
    url(r'^clientes-agora/', clientes.views.data_corrente),
    url(r'^comercial/', comercial.views.comercial),
    url(r'^comercial-agora/', comercial.views.data_corrente),
    url(r'^estoque/', estoque.views.estoque),
    url(r'^estoque-agora/', estoque.views.estoque_agora),
    url(r'^financeiro/', financeiro.views.financeiro),
    url(r'^financeiro-agora/', financeiro.views.financeiro_agora),
    url(r'^fornecedores/', fornecedores.views.fornecedores),
    url(r'^fornecedores-agora/', fornecedores.views.fornecedores_agora),
    url(r'^rh/', rh.views.rh),
    url(r'^rh-agora/', rh.views.rh_agora),
    url('gustavo', TemplateView.as_view(template_name='gustavo.html'))
]
