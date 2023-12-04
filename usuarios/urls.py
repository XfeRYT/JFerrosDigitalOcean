from django.urls import path

from usuarios.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar
from usuarios.views import sucursal_listar, sucursal_crear, sucursal_modificar, sucursal_eliminar


urlpatterns = [
    path('usuario/', usuario_listar, name="usuario" ),
    path('usuario/crear/', usuario_crear, name="usuario-crear" ),
    path('usuario/modificar/<int:pk>/', usuario_modificar, name="usuario-modificar" ),
    path('usuario/eliminar/<int:pk>/', usuario_eliminar, name="usuario-eliminar" ),
    
    
    path('sucursal/', sucursal_listar, name="sucursal" ),
    path('sucursal/crear/', sucursal_crear, name="sucursal-crear" ),
    path('sucursal/modificar/<int:pk>/', sucursal_modificar, name="sucursal-modificar" ),
    path('sucursal/eliminar/<int:pk>/', sucursal_eliminar, name="sucursal-eliminar" ),
     
]