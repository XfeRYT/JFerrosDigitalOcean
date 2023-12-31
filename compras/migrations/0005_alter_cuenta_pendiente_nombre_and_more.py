# Generated by Django 4.2.6 on 2023-11-01 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_alter_cuenta_pendiente_valor_restar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta_pendiente',
            name='nombre',
            field=models.CharField(max_length=45, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message='Este campo solo permite letras y espacios.')]),
        ),
        migrations.AlterField(
            model_name='cuenta_pendiente',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=45, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d{1,2})?$', message='Ingresa un número válido con hasta 2 decimales.'), django.core.validators.MinValueValidator(limit_value=1, message='El precio debe ser mayor que 0.')], verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='cuenta_pendiente',
            name='valor_restar',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=45, null=True, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d{1,2})?$', message='Ingresa un número válido con hasta 2 decimales.'), django.core.validators.MinValueValidator(limit_value=1, message='El precio debe ser mayor que 0.')], verbose_name='Valor a restar'),
        ),
    ]
