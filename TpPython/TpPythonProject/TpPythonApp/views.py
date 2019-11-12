# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from TpPythonApp.models import Producto,Categoria,Empresa,Pais
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
    empresa = Empresa.objects.get(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        categorias = empresa.categorias.all()
        productos = Producto.objects.none()
        for categoria in categorias:
            cant = Categoria.objects.filter(categoriaPadre=categoria.id).count()
            productos |= Producto.objects.filter(categoria=categoria.id)
            if (cant > 0):
                categoriasHijas = Categoria.objects.filter(categoriaPadre=categoria.id)
                for c in categoriasHijas:
                    productos |= Producto.objects.filter(categoria=c.id)
        for p in productos:
            url = 'https://api.cambio.today/v1/quotes/USD/'+Pais.objects.get(id=empresa.pais_id).codigo+'/json?key=2565|GMJKiRR3QLXUmyNqgxCC85^hV05UDmw_'
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
    empresa = Empresa.objects.get(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        valido = False
        categorias = empresa.categorias.all()
        for categoria in categorias:
            if(categoria.id==producto.categoria_id):
                valido=True
            else:
                cant = Categoria.objects.filter(categoriaPadre=categoria.id).count()
                if (cant > 0):
                    categoriasHijas = Categoria.objects.filter(categoriaPadre=categoria.id)
                    for c in categoriasHijas:
                        if(c.id==producto.categoria.id):
                            valido=True
        if(valido==True):
            url = 'https://api.cambio.today/v1/quotes/USD/'+Pais.objects.get(id=empresa.pais_id).codigo+'/json?key=2565|GMJKiRR3QLXUmyNqgxCC85^hV05UDmw_'
            args = {'quantity': int(producto.precio)}
            response = requests.get(url, params=args)
            response_json = response.json()
            producto.precio = response_json["result"]["amount"]
            serializer = ProductoDetalleSerializer(producto)
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(status=404, data={'status':'false','message':'no tiene acceso a esa categoria'})


def productos_por_categoria(request,codigoEmpresa,idCategoria):
    empresa = Empresa.objects.get(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        categoriasEmpresa = empresa.categorias.all()
        categoriaBuscada = Categoria.objects.get(id=idCategoria)
        productos = Producto.objects.none()
        for categoriaEmpresa in categoriasEmpresa:
            if(categoriaEmpresa.id==categoriaBuscada.id):
                productos |= Producto.objects.filter(categoria=categoriaBuscada.id)
                cant = Categoria.objects.filter(categoriaPadre=categoriaBuscada.id).count()
                if (cant > 0):
                    categoriasHijas = Categoria.objects.filter(categoriaPadre=categoriaBuscada.id)
                    for categoriaHija in categoriasHijas:
                            productos |= Producto.objects.filter(categoria=categoriaHija.id)
            else:
                cant = Categoria.objects.filter(categoriaPadre=categoriaBuscada.id).count()
                if(cant>0):
                    categoriasHijas = Categoria.objects.filter(categoriaPadre=categoriaBuscada.id)
                    for categoriaHija in categoriasHijas:
                        if(categoriaEmpresa.id == categoriaHija.id):
                            productos|=Producto.objects.filter(categoria=categoriaHija.id)
        serializer = ProductoSerializer(productos, many=True)
        response = JSONResponse(serializer.data)
        return response
    else:
        return JSONResponse(status=404, data={'status': 'false', 'message': 'no es una clave de acceso correcta'})
def categoria_list(request,codigoEmpresa):
    """
    lista todos los productos junto a su categoria, stock y su precio.
    :return: todos los productos
    """
    empresa = Empresa.objects.get(codigo=codigoEmpresa)
    if request.method == 'GET' and empresa:
        categoria = empresa.categorias.all()
        serializer = CategoriaSerializer(categoria,many=True)
        response = JSONResponse(serializer.data)
        return response