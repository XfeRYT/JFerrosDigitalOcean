from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from usuarios.models import Usuario
# Create your models here.

class Metododepago(models.Model):
    nombre = models.CharField(max_length=45,verbose_name="Metodo de pago", validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message="Este campo solo permite letras y espacios.")])
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.nombre,self.estado)
    class Meta:
        verbose_name_plural = "Metodosdepagos"
      

class Domicilio(models.Model):
    direccion= models.CharField(max_length=45,verbose_name="Dirección y Barrio")
    fecha_envio= models.DateField(verbose_name="Fecha envío", help_text="MM/DD/AAAA", null=True)
    fecha_entrega= models.DateField(verbose_name="Fecha entrega", help_text="MM/DD/AAAA" , null=True)
    fecha= models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA", auto_now=True)
    usuario=models.ForeignKey(Usuario, verbose_name=_("Usuario"), on_delete=models.CASCADE)
    
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s"%(self.direccion)
    class Meta:
        verbose_name_plural = "Domicilios"
        
class Venta(models.Model):
    fecha= models.DateField(auto_now=True, verbose_name="Fecha", help_text="MM/DD/AAAA")
    metododepago=models.ForeignKey(Metododepago, verbose_name=_("Método de pago"), on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario, verbose_name=_("Usuario"), on_delete=models.CASCADE)
    domicilio=models.ForeignKey(Domicilio, verbose_name=_("Domicilio"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.fecha,self.estado)
    class Meta:
        verbose_name_plural = "Ventas"

  