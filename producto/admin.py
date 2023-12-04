from django.contrib import admin
from producto.models import Producto
from producto.models import Marca
from producto.models import Categoria
from producto.models import Subcategoria
from producto.models import Unidades




# Register your models here.
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Unidades)



