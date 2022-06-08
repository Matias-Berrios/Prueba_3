from unicodedata import name
from django.urls import path
from .views import home, crearUsuario, bandana, correa, placa, tienda_lista, registros, modificar_registros, borrar_del_producto, tienda_principal

urlpatterns = [
    path('', home,name="home"),
    path('crearUsuario', crearUsuario,name="crearUsuario"),
    path('bandana', bandana,name="bandana"),
    path('correa', correa,name="correa"),
    path('placa', placa,name="placa"),
    path('tienda_lista', tienda_lista,name="tienda_lista"),
    path('registros', registros,name="registros"),
    path('modificar_registros/<id>', modificar_registros,name="modificar_registros"),
    path('borrar_del_producto/<id>', borrar_del_producto,name="borrar_del_producto"),
    path('tienda_principal', tienda_principal,name="tienda_principal")
]
