from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from decimal import Decimal
from django.core.validators import MinValueValidator


# Create your models here.

class Marca(models.Model):
    marca=models.CharField(max_length=45, verbose_name="Marca", validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', message="Este campo solo permite letras.")])
    
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def __str__(self):
        return "%s"%(self.marca)
    class Meta:
        verbose_name_plural = "Marcas"

class Unidades(models.Model):
    unidades=models.CharField(max_length=10,  validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    class Medida(models.TextChoices):
        pulgada="Pulgada",_("Pulgada")
        centimetro="Centimetro",_("Centimetro")
        milimetros="Milimetros",_("Milimetros")
        kilos="Kilos",_("Kilos")
        miligramos="Miligramos",_("Miligramos")       
        libras="Libras",_("Libras")
    medida=models.CharField(max_length=45, verbose_name="Medida",choices=Medida.choices)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.unidades, self.medida)
    class Meta:
        verbose_name_plural = "Unidades"
class Subcategoria(models.Model):
    nombre=models.CharField(max_length=45, validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', message="Este campo solo permite letras.")])
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s"%(self.nombre)
    class Meta:
        verbose_name_plural = "Subcategorias"

class Categoria(models.Model):
    class Subcategory(models.TextChoices):
        construccion="Construccion",_("Construcción")
        electricidad="Electricidad",_("Electricidad")
        herramientas_manual="Herramientas Manuales",_("Herramientas Manuales")
        plomeria_tuberias="Plomeria y Tuberias",_("Plomeria y Tuberias")
        equipos_proteccion="Equipos de protección",_("Equipos de protección")
    subcategory=models.CharField(max_length=45, verbose_name="Nombre",choices=Subcategory.choices)
    categoria = models.ForeignKey(Subcategoria, verbose_name="Subcategoria",  on_delete=models.CASCADE)

    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)

    def __str__(self):
        return "%s"%(self.categoria)
    class Meta:
        verbose_name_plural = "Categorias"



class Producto(models.Model):
    nombre=models.CharField(max_length=45, validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', message="Este campo solo permite letras.")])
    precio = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Precio"),
        validators=[MinValueValidator(limit_value=0.01, message=_("El precio debe ser mayor que cero."))]
    )    
    class Color(models.TextChoices):
        azul="1",_("Azul")
        rojo="2",_("Rojo")
        amarillo="3",_("Amarillo")
        verde="4",_("Verde")
        negro="5",_("Negro")
    color=models.CharField(max_length=45, verbose_name="Color",choices=Color.choices)
    class Presentacion(models.TextChoices):
        bolsa="1",_("Bolsa")
        caja="2",_("Caja")
    presentacion=models.CharField(max_length=45, verbose_name="Presentacion",choices=Presentacion.choices)
    class Material(models.TextChoices):
        metal="1",_("Metal")
        plastico="2",_("Plastico")
        hierro="3",_("Hierro")
    material=models.CharField(max_length=45, verbose_name="Material",choices=Material.choices)
    marca= models.ForeignKey(Marca, related_name='Marca',  on_delete=models.CASCADE)
    unidades= models.ForeignKey(Unidades, related_name='Unidades',  on_delete=models.CASCADE)
    categoria= models.ForeignKey(Categoria, related_name='Categoria',  on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45,  verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def clean(self):
        self.nombre=self.nombre.title()
    def __str__(self):
        return "%s %s"%(self.nombre, self.precio)
    def precio_colombiano(self):
        formatted_price = "{:,.2f}".format(self.precio).replace(',', '#').replace('.', ',').replace('#', '.')
        return f"${formatted_price}"
    class Meta:
        verbose_name_plural = "Productos"




