from django.contrib import admin
from ingreso_egreso.models import Stock
from ingreso_egreso.models import Detalle_Venta
from ingreso_egreso.models import Detalle_Compra

# Register your models here.
admin.site.register(Stock)
admin.site.register(Detalle_Compra)
admin.site.register(Detalle_Venta)
