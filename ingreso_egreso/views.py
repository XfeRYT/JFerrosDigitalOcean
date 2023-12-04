from django.shortcuts import render, redirect
from ingreso_egreso.models import Stock
from producto.models import Producto
from ventas.models import Venta
from compras.models import Compra
from ingreso_egreso.forms import StockForm, StockUpdateForm
from ingreso_egreso.models import Detalle_Compra
from ingreso_egreso.forms import Detalle_CompraForm, Detalle_CompraUpdateForm
from ingreso_egreso.models import Detalle_Venta
from ingreso_egreso.forms import Detalle_VentaForm, Detalle_VentaUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db import models
from django.db.models import Sum
from django.db.models import Sum, F, ExpressionWrapper, IntegerField
from django.db.models.functions import Coalesce
from decimal import Decimal


# Create your views here.
@login_required
def stock_crear(request):
    titulo = "Stock"

    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']
            # Obtén o crea el registro de stock para el producto
            stock, created = Stock.objects.get_or_create(producto=producto)
            # Actualiza la cantidad en stock
            stock.actualizar_stock_compra(cantidad)
            messages.success(request, "Stock actualizado correctamente.")
            return redirect("stock_listar")
    else:
        form = StockForm()
    context = {"form": form, "titulo": titulo}
    return render(request, "ingreso_egreso/stock/crear.html", context)



@login_required
def stock_listar(request):
    titulo = "Stock"
    modulo = "Ingreso_egreso"
    # Obtener la suma de las cantidades de detalles de compra por producto
    compra_cantidades = Detalle_Compra.objects.values('producto').annotate(total_comprado=Sum('cantidad'))
    # Obtener la suma de las cantidades de detalles de venta por producto
    venta_cantidades = Detalle_Venta.objects.values('producto').annotate(total_vendido=Sum('cantidad'))
    # Crear un diccionario que almacene la cantidad total por producto
    cantidad_por_producto = {}
    for compra in compra_cantidades:
        producto_id = compra['producto']
        cantidad_comprada = compra['total_comprado']
        cantidad_por_producto[producto_id] = cantidad_comprada

    for venta in venta_cantidades:
        producto_id = venta['producto']
        cantidad_vendida = venta['total_vendido']
        if producto_id in cantidad_por_producto:
            cantidad_por_producto[producto_id] -= cantidad_vendida
        else:
            cantidad_por_producto[producto_id] = -cantidad_vendida
    # Actualizar la cantidad en el stock
    for producto_id, cantidad_total in cantidad_por_producto.items():
        stock, _ = Stock.objects.get_or_create(producto_id=producto_id)
        stock.cantidad = cantidad_total
        # Buscar un detalle de venta válido (puede ser None)
        detalle_venta = Detalle_Venta.objects.filter(producto_id=producto_id).first()
        stock.detalle_venta = detalle_venta
        detalle_compra = Detalle_Compra.objects.filter(producto_id=producto_id).first()
        stock.detalle_compra = detalle_compra
        stock.save()
    # Obtener la lista de productos en stock actualizada
    stocks = Stock.objects.all()
    context = {"stocks": stocks, "titulo": titulo}
    return render(request, "ingreso_egreso/stock/listar.html", context)


def detalle_compra_crear(request):
    titulo = "Detalle Compra"
    
    if request.method == "POST":
        form = Detalle_CompraForm(request.POST)
        
        if form.is_valid():
            producto = form.cleaned_data.get('producto')
            cantidad = form.cleaned_data.get('cantidad')
            precio_str = form.cleaned_data.get('precio_str')
            precio_decimal = Decimal(precio_str) if precio_str else Decimal(0)
            
            # Verificar si ya existe un registro con el mismo producto
            detalle_compra_existente = Detalle_Compra.objects.filter(producto=producto).first()
            
            if detalle_compra_existente:
                # Si existe, sumar la cantidad y actualizar el precio
                detalle_compra_existente.cantidad += cantidad
                detalle_compra_existente.precio_compra += precio_decimal
                detalle_compra_existente.save()
            else:
                # Si no existe, crear un nuevo registro
                detalle_compra = Detalle_Compra(producto=producto, cantidad=cantidad, precio_compra=precio_decimal)
                detalle_compra.save()
            
            # Actualizar el stock
            stock, created = Stock.objects.get_or_create(producto=producto)
            stock.actualizar_stock_compra(cantidad)
            
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("detalle_compra")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Detalle_CompraForm()
        producto_activos = Producto.objects.filter(estado='1')
        form.fields['producto'].queryset = producto_activos
    
    context = {"titulo": titulo, "form": form, "user": request.user}
    return render(request, "ingreso_egreso/detalle_compra/crear.html", context)


def detalle_compra_listar(request, pk):
    titulo = "Detalle Compra"
    modulo = "Ingreso_egreso"
    compra = Compra.objects.get(id=pk)
    detalle_compras = Detalle_Compra.objects.filter(compra__id=pk)
    productos = Producto.objects.filter(estado="1")
    
    if request.method == "POST":
        form = Detalle_CompraForm(request.POST)
        
        if form.is_valid():
            producto = form.cleaned_data.get('producto')
            cantidad = form.cleaned_data.get('cantidad')
            precio_str = form.cleaned_data.get('precio_str')
            precio_decimal = Decimal(precio_str) if precio_str else Decimal(0)
            
            # Verificar si ya existe un registro con el mismo producto en la compra actual
            detalle_compra_existente = detalle_compras.filter(producto=producto).first()
            
            if detalle_compra_existente:
                # Si existe, sumar la cantidad y actualizar el precio
                detalle_compra_existente.cantidad += cantidad
                detalle_compra_existente.precio_compra += precio_decimal
                detalle_compra_existente.save()
            else:
                # Si no existe, crear un nuevo registro
                det_compra = form.save(commit=False)
                det_compra.compra = Compra.objects.get(id=pk)
                det_compra.save()
            
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("detalle_compra", pk)
        else:
            print(form.errors)
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Detalle_CompraForm()
    
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "detalle_compras": detalle_compras,
        "user": request.user,
        "compra": compra,
        "productos": productos
    }
    
    return render(request, "ingreso_egreso/detalle_compra/listar.html", context)

def detalle_compra_modificar(request, pk):
    titulo = "Detalle Compra"
    detalle_compra = Detalle_Compra.objects.get(id=pk)

    if request.method == "POST":
        form = Detalle_CompraUpdateForm(request.POST, instance=detalle_compra)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("detalle_compra")
    else:
        form = Detalle_CompraUpdateForm(instance=detalle_compra)
        producto_activos = Producto.objects.filter(estado='1')
        form.fields['producto'].queryset = producto_activos
        compas_activos = Compra.objects.filter(estado='1')
        form.fields['compra'].queryset = compas_activos
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "ingreso_egreso/detalle_compra/modificar.html", context)


def detalle_compra_eliminar(request, pk):
    detalle_compra = get_object_or_404(Detalle_Compra, id=pk)
    id_proy = detalle_compra.compra.id
    detalle_compra.delete()
    return redirect("detalle_compra", id_proy)

def detalle_venta_crear(request, pk):
    titulo = "Detalle Venta"
    
    if request.method == "POST":
        form = Detalle_VentaForm(request.POST)
        
        if form.is_valid():
            producto = form.cleaned_data.get('producto')
            cantidad = form.cleaned_data.get('cantidad')
            
            # Obtén el stock actual del producto
            stock = Stock.objects.get(producto=producto)
            
            if stock.cantidad >= cantidad:
                # Si hay suficientes existencias en el stock
                precio_str = form.cleaned_data.get('precio_str')
                precio_decimal = Decimal(precio_str) if precio_str else Decimal(0)
                
                # Verificar si ya existe un registro con el mismo producto en la venta
                detalle_venta_existente = Detalle_Venta.objects.filter(venta_id=pk, producto=producto).first()
                
                if detalle_venta_existente:
                    # Si existe, sumar la cantidad y actualizar el precio
                    detalle_venta_existente.cantidad += cantidad
                    detalle_venta_existente.precio_venta += precio_decimal
                    detalle_venta_existente.save()
                else:
                    # Si no existe, crear un nuevo registro
                    detalle_venta = form.save(commit=False)
                    detalle_venta.precio_venta = precio_decimal
                    detalle_venta.venta_id = pk  # Asigna el ID de la venta
                    detalle_venta.save()
                
                # Actualizar el stock
                stock.actualizar_stock_venta(cantidad)
                
                messages.success(request, "El formulario se ha enviado correctamente.")
                return redirect("detalle_venta")
            else:
                messages.error(request, "No hay suficientes existencias en el stock para este producto.")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Detalle_VentaForm()
        productos_activos = Producto.objects.filter(estado='1')
        form.fields['producto'].queryset = productos_activos
    
    context = {"titulo": titulo, "form": form, "user": request.user}
    return render(request, "ingreso_egreso/detalle_venta/crear.html", context)




def detalle_venta_listar(request, pk):
    titulo = "Detalle Venta"
    modulo = "Ingreso_egreso"
    venta = Venta.objects.get(id=pk)
    detalle_ventas = Detalle_Venta.objects.filter(venta__id=pk)
    productos = Producto.objects.filter(estado="1")

    if request.method == "POST":
        form = Detalle_VentaForm(request.POST)
        
        if form.is_valid():
            producto = form.cleaned_data.get('producto')
            cantidad = form.cleaned_data.get('cantidad')
            # Obtén el stock actual del producto
            stock = Stock.objects.get(producto=producto)
            
            if stock.cantidad >= cantidad:
                # Si hay suficientes existencias en el stock
                precio_str = form.cleaned_data.get('precio_str')
                precio_decimal = Decimal(precio_str) if precio_str else Decimal(0)
                # Verificar si ya existe un registro con el mismo producto en la venta actual
                detalle_venta_existente = Detalle_Venta.objects.filter(venta_id=pk, producto=producto).first()
            
                if detalle_venta_existente:
                    # Si existe, sumar la cantidad y actualizar el precio
                    detalle_venta_existente.cantidad += cantidad
                    detalle_venta_existente.precio_venta += precio_decimal
                    detalle_venta_existente.save()
                else:
                    # Si no existe, crear un nuevo registro
                    detalle_venta = form.save(commit=False)
                    detalle_venta.precio_venta = precio_decimal
                    detalle_venta.venta_id = pk  # Asigna el ID de la venta
                    detalle_venta.save()
                # Actualizar el stock
                stock.actualizar_stock_venta(cantidad)
                messages.success(request, "El formulario se ha enviado correctamente.")
                return redirect("detalle_venta", pk)
            else:
                messages.error(request, "No hay suficientes existencias en el stock para este producto.")
        else:
            print(form.errors)
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Detalle_VentaForm()
    
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "detalle_ventas": detalle_ventas,
        "user": request.user,
        "productos": productos,
        "venta": venta
    }
    
    return render(request, "ingreso_egreso/detalle_venta/listar.html", context)



def detalle_venta_modificar(request, pk):
    titulo = "Detalle Venta"
    detalle_venta = Detalle_Venta.objects.get(id=pk)

    if request.method == "POST":
        form = Detalle_VentaUpdateForm(request.POST, instance=detalle_venta)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("detalle_venta")
    else:
        form = Detalle_VentaUpdateForm(instance=detalle_venta)
        productos_activos = Producto.objects.filter(estado='1')
        form.fields['nombre'].queryset = productos_activos
        ventas_activos = Venta.objects.filter(estado='1')
        form.fields['venta'].queryset = ventas_activos
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "ingreso_egreso/detalle_venta/modificar.html", context)

def detalle_venta_eliminar(request, pk):
    detalle_venta = get_object_or_404(Detalle_Venta, id=pk)
    id_proy = detalle_venta.venta.id
    detalle_venta.delete()
    return redirect("detalle_venta", id_proy)

def detalle_venta_finalizar(request, pk):
    venta = Venta.objects.filter(id=pk)
    venta.update(estado="0")
    return redirect('venta')

    
def venta_final(request, venta_id):
    venta = Venta.objects.get(pk=venta_id)
    detalle_venta = Detalle_Venta.objects.filter(venta=venta)
    context = {
        'venta': venta,
        'detalle_ventas': detalle_venta,
    }
    return render(request, "ingreso_egreso/detalle_venta/venta_final.html", context)

def detalle_compra_finalizar(request, pk):
    compra = Compra.objects.get(id=pk)
    compra.estado = "0"
    compra.save()
    
    # Redirect to the 'compra' view with the compra_id as a parameter
    return redirect('compra')

    
def compra_final(request, compra_id):
    titulo = "Detalle compra"
    compra = Compra.objects.get(pk=compra_id)  # Suponiendo que hay una relación entre Venta y Compra
    detalle_compra = Detalle_Compra.objects.filter(compra=compra)
    context = {
        'titulo': titulo,
        'compra': compra,
        'detalle_compras': detalle_compra,
    }
    return render(request, "ingreso_egreso/detalle_compra/compra_final.html", context)