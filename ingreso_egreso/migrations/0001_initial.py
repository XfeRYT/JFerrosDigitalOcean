# Generated by Django 4.2.5 on 2023-10-10 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_compra', models.DecimalField(decimal_places=3, max_digits=45, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d{1,2})?$', message='Ingresa un número válido con hasta 2 decimales.')], verbose_name='Precio de compra')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1, message='La cantidad debe ser mayor que 0')])),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=45, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Detalles de compras',
            },
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1, message='La cantidad debe ser mayor que 0')])),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=45, verbose_name='Estado')),
                ('precio_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_venta_precio_venta', to='producto.producto', verbose_name='Precio de venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_venta_producto', to='producto.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name_plural': 'Detalles de ventas',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=1, message='La cantidad debe ser mayor que 0')])),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=45, verbose_name='Estado')),
                ('detalle_compra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ingreso_egreso.detalle_compra')),
                ('detalle_venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ingreso_egreso.detalle_venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto', verbose_name='Nombre')),
            ],
            options={
                'verbose_name_plural': 'Stocks',
            },
        ),
    ]
