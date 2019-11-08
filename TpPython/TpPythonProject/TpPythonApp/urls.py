from django.conf.urls import url
from TpPythonApp import views


urlpatterns = [
    url(r'^(?P<codigoEmpresa>\w{0,50})/productos/$', views.producto_list),
    url(r'^categorias/$', views.categoria_list),
    url(r'^precios/$', views.precios_list),
    url(r'^(?P<codigoEmpresa>\w{0,50})/productos/(?P<pk>[0-9]+)/$', views.producto_detalle),
]
