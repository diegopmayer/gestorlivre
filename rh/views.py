from django.shortcuts import render
from django.http import HttpResponse
import datetime

def rh(request):
    return HttpResponse('RH')

def rh_agora(request):
    agora = datetime.datetime.now()
    html = "<html><body> HTML de RH - agora: %s.</body></html>" % agora
    return HttpResponse(html)
