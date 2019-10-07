#archivo creado para serializar.
from rest_framework import serializers
from .models import Producto,Precio,Categoria,Empresa


class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ('precio','fechaPrecio')

class ProductoSerializer(serializers.ModelSerializer):
    precios = PrecioSerializer(many=True)
    class Meta:
        model = Producto
        fields = ('id','nombre','cantidad','precios')

