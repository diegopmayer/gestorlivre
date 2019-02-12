from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index_clientes(request):
    return HttpResponse('Clientes')

def data_corrente(request):
    agora = datetime.datetime.now()
    html = "<html><body>Agora é %s.</body></html>" % agora
    return HttpResponse(html)
    