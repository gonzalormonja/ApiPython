# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=255)
    cantidadProducto = models.IntegerField(default=0)
    precioProducto = models.FloatField()
    categoriaProducto = models.CharField(max_length=255)

