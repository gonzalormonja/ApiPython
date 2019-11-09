# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from TpPythonApp.models import Producto,Categoria,Empresa
from TpPythonApp.serializers import ProductoSerializer,CategoriaSerializer,ProductoDetalleSerializer
from django.shortcuts import render
from rest_framework.exceptions import NotFound
import requests


# Create your views here.
class JSONResponse(HttpResponse):
    """
    muestra la respuesta en json
    """
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)
def producto_list(request,codigoEmpresa):
    """
    lista todos los productos junto a su categoria, stock y su precio.
    :return: todos los productos
    """
    empresa = Empresa.objects.filter(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        productos = Producto.objects.all()
        for p in productos:
            url = 'https://api.cambio.today/v1/quotes/USD/ARS/json?key=2565|GMJKiRR3QLXUmyNqgxCC85^hV05UDmw_'
            args = {'quantity':int(p.precio)}
            response = requests.get(url,params=args)
            response_json = response.json()
            p.precio = response_json["result"]["amount"]
        serializer = ProductoSerializer(productos,many=True)
        response = JSONResponse(serializer.data)
        return response

def producto_detalle(request,idProducto,codigoEmpresa):
    """
    obtener un solo producto
    :param pk: id del producto
    :return: el producto
    """
    try:
        producto = Producto.objects.get(pk=idProducto)
    except Producto.DoesNotExist:
        return HttpResponse(status=404)
    empresa = Empresa.objects.filter(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        serializer = ProductoDetalleSerializer(producto)
        return JSONResponse(serializer.data)

def productos_por_categoria(request,codigoEmpresa,idCategoria):
    empresa = Empresa.objects.filter(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        cant = Categoria.objects.filter(categoriaPadre=idCategoria).count()
        producto = Producto.objects.filter(categoria=idCategoria)
        if(cant>0):
            categorias = Categoria.objects.filter(categoriaPadre=idCategoria)
            for categoria in categorias:
                if(categoria.id!=idCategoria):
                    producto |= Producto.objects.filter(categoria=categoria.id)
        serializer = ProductoSerializer(producto, many=True)
        response = JSONResponse(serializer.data)
        return response

def categoria_list(request,codigoEmpresa):
    """
    lista todos los productos junto a su categoria, stock y su precio.
    :return: todos los productos
    """
    empresa = Empresa.objects.filter(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria,many=True)
        response = JSONResponse(serializer.data)
        return response