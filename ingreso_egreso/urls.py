from django.urls import path
from ingreso_egreso.views import stock_listar, stock_crear
from ingreso_egreso.views import detalle_compra_listar, detalle_compra_crear, detalle_compra_modificar, detalle_compra_eliminar, detalle_venta_finalizar, venta_final
from ingreso_egreso.views import detalle_venta_listar, detalle_venta_crear, detalle_venta_modificar, detalle_venta_eliminar, detalle_compra_finalizar, compra_final


urlpatterns = [
    path('stock/', stock_listar, name="stock" ),
    path('crear/', stock_crear, name="stock-crear" ),
    
    
    path('detalle_compra/<int:pk>/', detalle_compra_listar, name="detalle_compra" ),
    path('detalle_compra/crear/', detalle_compra_crear, name="detalle_compra-crear" ),
    path('detalle_compra/modificar/<int:pk>/', detalle_compra_modificar, name="detalle_compra-modificar" ),
    path('detalle compra/eliminar/<int:pk>/', detalle_compra_eliminar, name="detalle_compra-eliminar" ),

    path('detalle_venta/<int:pk>/', detalle_venta_listar, name="detalle_venta" ),
    path('detalle_venta/crear/', detalle_venta_crear, name="detalle_venta-crear" ),
    path('detalle_venta/modificar/<int:pk>/', detalle_venta_modificar, name="detalle_venta-modificar" ),
    path('detalle venta/eliminar/<int:pk>/', detalle_venta_eliminar, name="detalle_venta-eliminar" ),
    
    path('detalle_venta/finalizar/<int:pk>/', detalle_venta_finalizar, name="detalle_venta-finalizar"),
    path('ingreso_egreso/detalle_venta/venta_final/<int:venta_id>/', venta_final, name='venta_final'),


    path('detalle_compra/finalizar/<int:pk>/', detalle_compra_finalizar, name='detalle_compra-finalizar'),
    path('ingreso_egreso/detalle_compra/compra_final/<int:compra_id>/', compra_final, name='compra_final'),
]
