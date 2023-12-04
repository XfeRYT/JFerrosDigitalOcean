from django.db import models
from usuarios.models import Usuario
from producto.models import Producto
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.validators import RegexValidator, MinValueValidator


# Create your models here.

        
class Cuenta_Pendiente(models.Model):
    nombre=models.CharField(max_length=45, verbose_name="Nombre del proveedor",validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message="Este campo solo permite letras y espacios.")])
    nombre_producto = models.ForeignKey(Producto,  verbose_name=_("Nombre del Producto"), on_delete=models.CASCADE)
    fecha_inicio=models.DateField(verbose_name="Fecha de Inicio",  help_text="MM/DD/AAAA", auto_now=True)
    valor=models.DecimalField(max_digits=45, decimal_places=2, verbose_name="Precio pendiente",validators=[RegexValidator(r'^\d+(\.\d{1,2})?$', message="Ingresa un número válido con hasta 2 decimales."), MinValueValidator(limit_value=1, message="El precio debe ser mayor que 0.")])
    valor_restar = models.DecimalField(max_digits=45, decimal_places=2, verbose_name="Pagar", null=True, blank=True, validators=[RegexValidator(r'^\d+(\.\d{1,2})?$', message="Ingresa un número válido con hasta 2 decimales."), MinValueValidator(limit_value=1, message="El precio debe ser mayor que 0.")])
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=15, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s"%(self.nombre)
    def precio_colombiano(self):
        formatted_price = "{:,.2f}".format(self.valor).replace(',', '#').replace('.', ',').replace('#', '.')
        return f"${formatted_price}"
    class Meta:
        verbose_name_plural = "Cuentas Pendientes"


class Compra(models.Model):
    fecha=models.DateField(verbose_name="Fecha",  help_text="MM/DD/AAAA", auto_now=True)
    usuario=models.ForeignKey(Usuario,  verbose_name=_("Usuario"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=15, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.fecha,self.estado)
    class Meta:
        verbose_name_plural = "Compras"
   