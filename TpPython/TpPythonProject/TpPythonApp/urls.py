from django.conf.urls import url
from TpPythonApp import views


urlpatterns = [
    url(r'^(?P<codigoEmpresa>\w{0,50})/productos/$', views.producto_list),
    url(r'^(?P<codigoEmpresa>\w{0,50})/categorias/$', views.categoria_list),
    url(r'^(?P<codigoEmpresa>\w{0,50})/productos/(?P<idProducto>[0-9]+)/$', views.producto_detalle),
    url(r'^(?P<codigoEmpresa>\w{0,50})/productosCategoria/(?P<idCategoria>[0-9]+)/$', views.productos_por_categoria),
]
