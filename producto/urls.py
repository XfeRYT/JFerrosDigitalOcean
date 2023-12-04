from django.urls import path

from producto.views import producto_listar, producto_crear, producto_modificar, producto_eliminar
from producto.views import marca_listar, marca_crear, marca_modificar, marca_eliminar
from producto.views import unidades_listar, unidades_crear, unidades_modificar, unidades_eliminar
from producto.views import subcategoria_listar, subcategoria_crear, subcategoria_modificar, subcategoria_eliminar
from producto.views import categoria_listar, categoria_crear, categoria_modificar, categoria_eliminar


urlpatterns = [
    path('producto/', producto_listar, name="producto" ),
    path('producto/crear/', producto_crear, name="producto-crear" ),
    path('producto/modificar/<int:pk>/', producto_modificar, name="producto-modificar" ),
    path('producto/eliminar/<int:pk>/', producto_eliminar, name="producto-eliminar" ),
    
    
    path('marca/', marca_listar, name="marca" ),
    path('marca/crear/', marca_crear, name="marca-crear" ),
    path('marca/modificar/<int:pk>/', marca_modificar, name="marca-modificar" ),
    path('marca/eliminar/<int:pk>/', marca_eliminar, name="marca-eliminar" ),
    
    path('unidades/', unidades_listar, name="unidades" ),
    path('unidades/crear/', unidades_crear, name="unidades-crear" ),
    path('unidades/modificar/<int:pk>/', unidades_modificar, name="unidades-modificar" ),
    path('unidades/eliminar/<int:pk>/', unidades_eliminar, name="unidades-eliminar" ),
    
    path('subcategoría/', subcategoria_listar, name="subcategoria" ),
    path('subcategoría/crear/', subcategoria_crear, name="subcategoria-crear" ),
    path('subcategoría/modificar/<int:pk>/', subcategoria_modificar, name="subcategoria-modificar" ),
    path('subcategoría/eliminar/<int:pk>/', subcategoria_eliminar, name="subcategoria-eliminar" ),
    
    path('categoria/', categoria_listar, name="categoria" ),
    path('categoría/crear/', categoria_crear, name="categoria-crear" ),
    path('categoría/modificar/<int:pk>/', categoria_modificar, name="categoria-modificar" ),
    path('categoría/eliminar/<int:pk>/', categoria_eliminar, name="categoria-eliminar" ),
]
