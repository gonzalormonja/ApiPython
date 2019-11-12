#archivo creado para serializar.
from rest_framework import serializers
from .models import Producto,Categoria,Empresa,Foto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields=('id','nombre')



class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source='categoria.nombre')
    fotos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
     )
    class Meta:
        model = Producto
        fields = ('id','nombre','cantidad','categoria','fotos','precio')


class ProductoDetalleSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source='categoria.nombre')
    fotos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )
    class Meta:
        model = Producto
        fields = ('id','nombre','cantidad','categoria','descripcion','fotos','precio')