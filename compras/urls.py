from django.urls import path

from compras.views import compra_listar, compra_crear, compra_modificar, compra_eliminar
from compras.views import cuenta_pendiente_listar, cuenta_pendiente_crear, cuenta_pendiente_modificar, cuenta_pendiente_eliminar


urlpatterns = [
    path('compras/', compra_listar, name="compra" ),
    path('compras/crear/', compra_crear, name="compra-crear" ),
    path('compras/modificar/<int:pk>/', compra_modificar, name="compra-modificar" ),
    path('compra/eliminar/<int:pk>/', compra_eliminar, name="compra-eliminar" ),

    path('cuentaspendientes', cuenta_pendiente_listar, name="cuenta_pendiente" ),
    path('cuentaspendientes/crear/', cuenta_pendiente_crear, name="cuenta_pendiente-crear" ),
    path('cuentaspendientes/modificar/<int:pk>/', cuenta_pendiente_modificar, name="cuenta_pendiente-modificar" ),
    path('cuenta pendiente/eliminar/<int:pk>/', cuenta_pendiente_eliminar, name="cuenta_pendiente-eliminar" ),
    
]