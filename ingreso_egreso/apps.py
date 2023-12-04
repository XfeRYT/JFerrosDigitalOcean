from django.apps import AppConfig
class StockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock'
class Detalle_CompraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'detalle_compra'
class Detalle_VentaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'detalle_venta'
