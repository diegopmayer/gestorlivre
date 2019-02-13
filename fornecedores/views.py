from django.shortcuts import render
from django.http import HttpResponse
import datetime

def fornecedores(request):
    return HttpResponse('Fornecedores')

def fornecedores_agora(request):
    agora = datetime.datetime.now()
    html =  "<html><body> HTML em Fornecedores - agora: %s." % agora
    return HttpResponse(html)
