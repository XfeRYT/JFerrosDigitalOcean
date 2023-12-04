from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nombre =models.CharField(max_length=45, null=False, blank=False, validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message="Este campo solo permite letras y espacios.")])
    apellido=models.CharField(max_length=45, null=False, blank=False, validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message="Este campo solo permite letras y espacios.")])
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula Ciudadania")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento=models.CharField(max_length=2, choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=10,  validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    telefono=models.CharField(max_length=10,  validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    direccion=models.CharField(max_length=15, verbose_name="Dirección")
    correo=models.EmailField(unique=True, validators=[EmailValidator(message="Por favor, ingresa una dirección de correo electrónico válida.")])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarios', null=True, blank=True)
    rol = models.ForeignKey(Group, verbose_name="Rol", on_delete=models.SET_NULL, null=True, blank=True)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado", choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.nombre, self.apellido)
    class Meta:
        verbose_name_plural = "Usuarios"

class Sucursal(models.Model):
    direccion=models.CharField(max_length=45, verbose_name="Dirección")
    municipio=models.CharField(max_length=45, validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message="Este campo solo permite letras.")])
    telefono=models.CharField(max_length=10, verbose_name="Teléfono", validators=[RegexValidator(r'^\d+$ ', message="Este campo solo permite números.")])
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="0",_("Inactivo")
    estado=models.CharField(max_length=45, verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s"%(self.municipio)
    class Meta:
        verbose_name_plural = "Sucursales"