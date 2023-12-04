from django.contrib import admin
from ventas.models import Venta
from ventas.models import Metododepago
from ventas.models import Domicilio


# Register your models here.
admin.site.register(Venta)
admin.site.register(Metododepago)
admin.site.register(Domicilio)
