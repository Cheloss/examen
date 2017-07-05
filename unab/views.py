# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unab.models import Noticia
from django.shortcuts import render, get_object_or_404
from unab.forms import NoticiaForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from sorl.thumbnail import get_thumbnail

def noticia_list(request):
    data = {}

    data['object_list'] = Noticia.objects.all().order_by('-created')


    template_name = 'noticia/noticia_list.html'
    return render(request, template_name, data)

def noticia_update(request, pk) :
    data = {}

    data['object_list'] = Noticia.objects.filter(pk=pk)
    template_name = 'noticia/noticia_detalle.html'
    return render(request, template_name, data)
def unab_contactos(request) :
    data = {}

    data['object_list'] = Noticia.objects.all().order_by('-created')
    template_name = 'noticia/contactos.html'
    return render(request, template_name, data)

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
