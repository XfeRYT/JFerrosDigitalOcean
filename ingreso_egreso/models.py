from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from ventas.models import Venta
from compras.models import Compra
from producto.models import Producto
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

# Create your models here.
class Detalle_Venta(models.Model):
    producto = models.ForeignKey(Producto, verbose_name="Producto", on_delete=models.CASCADE)
    cantidad=models.IntegerField(
        validators=[MinValueValidator(limit_value=1, message="La cantidad debe ser mayor que 0")]
    )    
    venta=models.ForeignKey(Venta,  verbose_name=_("Venta"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return f"{self.producto} - Precio: {self.precio_venta}"
    def subtotal(self):
        return self.cantidad * self.producto.precio
    def subtotal_colombiano(self):
        formatted_subtotal = "{:,.2f}".format(self.subtotal()).replace(',', '#').replace('.', ',').replace('#', '.')
        return f"${formatted_subtotal}"
    class Meta:
        verbose_name_plural = "Detalles de ventas"

class Detalle_Compra(models.Model):
    producto=models.ForeignKey(Producto,  verbose_name="Nombre", on_delete=models.CASCADE)
    precio_compra=models.DecimalField(max_digits=45, decimal_places=2, verbose_name="Precio de compra", validators=[MinValueValidator(limit_value=1, message="El precio de compra debe ser mayor que 0.")])
    cantidad = models.IntegerField(
        validators=[MinValueValidator(limit_value=1, message="La cantidad debe ser mayor que 0")]
    )
    compra=models.ForeignKey(Compra, verbose_name=_("Compra"),  on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.producto,self.precio_compra)
    def subtotal(self):
        return self.cantidad * self.precio_compra
    def subtotal_colombiano(self):
        formatted_subtotal = "{:,.2f}".format(self.subtotal()).replace(',', '#').replace('.', ',').replace('#', '.')
        return f"${formatted_subtotal}"
    def precio_colombiano(self):
        formatted_price = "{:,.2f}".format(self.precio_compra).replace(',', '#').replace('.', ',').replace('#', '.')
        return f"${formatted_price}"

    class Meta:
        verbose_name_plural = "Detalles de compras"
        
class Stock(models.Model):
    producto=models.ForeignKey(Producto,  verbose_name="Nombre", on_delete=models.CASCADE)
    cantidad = models.IntegerField(
        validators=[MinValueValidator(limit_value=1, message="La cantidad debe ser mayor que 0")],
        null=True,  # Permitir valores nulos
        default=0    # Valor predeterminado
    )
    detalle_venta = models.ForeignKey(Detalle_Venta, on_delete=models.CASCADE, null=True, blank=True)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return str(self.cantidad)

    class Meta:
        verbose_name_plural = "Stocks"

    def actualizar_stock_venta(self, cantidad_restar):
        """
        Actualiza la cantidad de stock restando la cantidad especificada.
        """
        if cantidad_restar <= self.cantidad:
            self.cantidad -= cantidad_restar
            self.save()
            return True
        else:
            return False

    def actualizar_stock_compra(self, cantidad_sumar):
        """
        Actualiza la cantidad de stock sumando la cantidad especificada.
        """
        if cantidad_sumar >= 0:
            self.cantidad += cantidad_sumar
            self.save()
            return True
        else:
            return False
    def __str__(self):
        return "%s"%(self.cantidad)
    class Meta:
        verbose_name_plural = "Stocks"
        
