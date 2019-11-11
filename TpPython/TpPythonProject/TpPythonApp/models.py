# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    categoriaPadre = models.ForeignKey('self',null=True,blank=True,related_name='subcategorias')


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=2000,default="")
    categoria = models.ForeignKey('Categoria')
    precio = models.FloatField(default=0)


class Foto(models.Model):
    url = models.CharField(max_length=255,default="")
    producto = models.ForeignKey('Producto',related_name='fotos')

class Pais(models.Model):
    nombre = models.CharField(max_length=255,default="")
    codigo = models.CharField(max_length=255,default="")

class Empresa(models.Model):
    codigo = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255,default="sinNombre")
    categorias = models.ManyToManyField('Categoria')
    pais = models.ForeignKey('Pais',default=None)