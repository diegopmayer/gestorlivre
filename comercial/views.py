from django.shortcuts import render
from django.http import HttpResponse
import datetime

def comercial(request):
    return HttpResponse('Comercial')

def data_corrente(request):
    agora = datetime.datetime.now()
    html = "<html><body>agora html %s. </body></html>" % agora
    return HttpResponse(html)
