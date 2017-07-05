# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


    
class Category(models.Model):
    name = models.CharField(max_length=144)
    sort_order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Noticia(models.Model):
    name = models.CharField(max_length=20)
    contenido = models.TextField()
    category = models.ForeignKey(Category)
    sort_order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
        
class Contactos(models.Model):
    name = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=60)
    imagen=models.ImageField()
    def __str__(self):
        return self.name 


# class Album(models.Model):
#     name = models.CharField(max_length=144) 
#     anio = models.PositiveIntegerField()
#     # picture = models.ImageField(upload_to='album/', default='album/no-image.jpg')
#     order = models.IntegerField()
    

# class Song(models.Model):
#     name = models.CharField(max_length=144) 
#     minutes = models.PositiveIntegerField()
#     seconds = models.PositiveIntegerField()
#     # track_number = models.PositiveIntegerField()
#     album = models.ForeignKey(Album)

#     def duration(self):
#         return '%d:%d' % (self.minutes,self.seconds)