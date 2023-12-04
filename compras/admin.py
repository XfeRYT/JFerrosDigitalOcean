from django.contrib import admin
from compras.models import Compra
from compras.models import Cuenta_Pendiente

# Register your models here.
admin.site.register(Compra)
admin.site.register(Cuenta_Pendiente)
