from django.urls import path
from inicio.views import inicio, acerca, agregar_producto_view, ver_pedido_view, eliminar_producto, editar_producto


urlpatterns = [
     path('', inicio, name= 'inicio'),
     path('acerca/', acerca, name= 'acerca'),
     path('agregar_producto/', agregar_producto_view, name= 'agregar_producto'),
     path('ver_pedido/', ver_pedido_view, name= 'ver_pedido'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:id>/', editar_producto, name='editar_producto')


]


