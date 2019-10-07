# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models






class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    categoriaPadre = models.ForeignKey('self',null=True,blank=True,related_name='subcategorias')

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField(default=0)
    categoria = models.ForeignKey('Categoria')

class Precio(models.Model):
    precio = models.FloatField()
    fechaPrecio = models.DateField()
    producto = models.ForeignKey('Producto',related_name='precios')

class Empresa(models.Model):
    codigo = models.CharField(max_length=255)
    categorias = models.ManyToManyField('Categoria')