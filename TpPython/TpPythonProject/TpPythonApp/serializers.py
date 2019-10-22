#archivo creado para serializar.
from rest_framework import serializers
from .models import Producto,Precio,Categoria,Empresa


class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ('id','precio','fechaPrecio')




class CategoriaParaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria

        fields=('id','nombre')


class ProductoSerializer(serializers.ModelSerializer):
    precios = PrecioSerializer(many=True)
    categoria_set = serializers.ReadOnlyField(source='categoria.nombre')
    class Meta:
        model = Producto
        fields = ('id','nombre','cantidad','categoria_set','precios')