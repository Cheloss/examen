# -*- coding: utf-8 -*-
from django.forms import ModelForm
from unab.models import Noticia
class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['name','contenido','category']
