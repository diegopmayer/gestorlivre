from django.shortcuts import render
from django.http import HttpResponse
import datetime

def financeiro(request):
    return HttpResponse('Financeiro')

def financeiro_agora(request):
    agora = datetime.datetime.now
    html = "<html><body> HTML em Financeiro - agora: %s.</body><html>" % agora
    return HttpResponse(html)
