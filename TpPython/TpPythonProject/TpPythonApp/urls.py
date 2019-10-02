from django.conf.urls import url
from TpPythonApp import views


urlpatterns = [
    url(r'^productos/$', views.producto_list),
    url(r'^productos/(?P<pk>[0-9]+)/$', views.producto_detalle),
]
