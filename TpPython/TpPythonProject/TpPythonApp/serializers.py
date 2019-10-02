#archivo creado para serializar.
from rest_framework import serializers
from .models import Producto


#esta seria una forma de crear el serializer manualmente
"""class ProductoSerializer(serializers.Serializer):
    #esta es la clave primaria del producto(id)
    pk = serializers.IntegerField(read_only=True)
    nombreProducto = serializers.CharField()
    cantidadProducto = serializers.IntegerField()
    precioProducto = serializers.FloatField()
    categoriaProducto = serializers.CharField()
"""
#esta es una forma de valernos de django para crearlo, esto crea automaticamente el metodo save y el metodo update.
#Lo cual para nuestros fines no es util
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombreProducto','cantidadProducto','precioProducto','categoriaProducto')