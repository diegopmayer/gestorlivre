from django.shortcuts import render
from django.http import HttpResponse
import datetime

def estoque(request):
    return HttpResponse('estoque')

def estoque_agora(request):
    agora = datetime.datetime.now()
    html = "<html><body> Html estoque agora %s.</body></html>" % agora
    return HttpResponse(html)
