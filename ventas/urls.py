from django.urls import path

from ventas.views import venta_listar, venta_crear, venta_modificar, venta_eliminar
from ventas.views import metododepago_listar, metododepago_crear, metododepago_modificar, metododepago_eliminar
from ventas.views import domicilio_listar, domicilio_crear, domicilio_modificar, domicilio_eliminar
urlpatterns = [
    path('venta/', venta_listar, name="venta" ),
    path('venta/crear/', venta_crear, name="venta-crear" ),
    path('venta/modificar/<int:pk>/', venta_modificar, name="venta-modificar" ),
    path('venta/eliminar/<int:pk>/', venta_eliminar, name="venta-eliminar" ),
    
    
    path('método de pago/', metododepago_listar, name="metododepago" ),
    path('método de pago/crear/', metododepago_crear, name="metododepago-crear" ),
    path('método de pago/modificar/<int:pk>/', metododepago_modificar, name="metododepago-modificar" ),
    path('método de pago/eliminar/<int:pk>/', metododepago_eliminar, name="metododepago-eliminar" ),
    
    
    path('domicilio/', domicilio_listar, name="domicilio" ),
    path('domicilio/crear/', domicilio_crear, name="domicilio-crear" ),
    path('domicilio/modificar/<int:pk>/', domicilio_modificar, name="domicilio-modificar" ),
    path('domicilio/eliminar/<int:pk>/', domicilio_eliminar, name="domicilio-eliminar" ),
]