from django.apps import AppConfig


class ProductoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'producto'
class MarcaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marca'
class CategoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categoria'
class SubcategoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subcategoria'
class UnidadesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'unidades'