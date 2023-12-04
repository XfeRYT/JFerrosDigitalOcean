from django.shortcuts import render, redirect
from producto.models import Producto
from producto.forms import ProductoForm, ProductoUpdateForm
from producto.models import Marca
from producto.forms import MarcaForm, MarcaUpdateForm
from producto.models import Unidades
from producto.forms import UnidadesForm, UnidadesUpdateForm
from producto.models import Subcategoria
from producto.forms import SubcategoriaForm, SubcategoriaUpdateForm
from producto.models import Categoria
from producto.forms import CategoriaForm, CategoriaUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal


# Create your views here.
@login_required
def producto_crear(request):
    titulo = "Producto"
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            precio_decimal = Decimal(form.cleaned_data['precio_str'])  # Convierte la cadena en un valor decimal
            producto.precio = precio_decimal
            producto.save()
            messages.success(request, "El producto se ha creado correctamente.")
            return redirect("producto")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = ProductoForm()
        marca_activos = Marca.objects.filter(estado='1')
        form.fields['marca'].queryset = marca_activos
        unidades_activos = Unidades.objects.filter(estado='1')
        form.fields['unidades'].queryset = unidades_activos
        categoria_activos = Categoria.objects.filter(estado='1')
        form.fields['categoria'].queryset = categoria_activos
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/producto/crear.html", context)

@login_required
def producto_listar(request):
    titulo = "Producto"
    modulo = "Producto"
    productos = Producto.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "productos": productos, "user":request.user}
    return render(request, "producto/producto/listar.html", context)

@login_required
def producto_modificar(request, pk):
    titulo = "Producto"
    producto = Producto.objects.get(id=pk)

    if request.method == "POST":
        form = ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("producto")
    else:
        form = ProductoUpdateForm(instance=producto)
        marca_activos = Marca.objects.filter(estado='1')
        form.fields['marca'].queryset = marca_activos
        unidades_activos = Unidades.objects.filter(estado='1')
        form.fields['unidades'].queryset = unidades_activos
        categoria_activos = Categoria.objects.filter(estado='1')
        form.fields['categoria'].queryset = categoria_activos
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/producto/modificar.html", context)

@login_required
def producto_eliminar(request, pk):
    producto = Producto.objects.filter(id=pk)
    producto.update(estado="0")
    return redirect("producto")

@login_required
def marca_crear(request):
    titulo = "Marca"
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("producto")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = MarcaForm()
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/marca/crear.html", context)

@login_required
def marca_listar(request):
    titulo = "Marca"
    modulo = "Producto"
    marcas = Marca.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "marcas": marcas, "user":request.user}
    return render(request, "producto/marca/listar.html", context)

@login_required
def marca_modificar(request, pk):
    titulo = "Marca"
    marca = Marca.objects.get(id=pk)

    if request.method == "POST":
        form = MarcaUpdateForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("marca")
    else:
        form = MarcaUpdateForm(instance=marca)
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/marca/modificar.html", context)

@login_required
def marca_eliminar(request, pk):
    marca = Marca.objects.filter(id=pk)
    marca.update(estado="0")
    return redirect("marca")

@login_required
def unidades_crear(request):
    titulo = "Unidades"
    if request.method == "POST":
        form = UnidadesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("producto")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = UnidadesForm()
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/unidades/crear.html", context)

@login_required
def unidades_listar(request):
    titulo = "Unidades"
    modulo = "Producto"
    unidades = Unidades.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "unidades": unidades, "user":request.user}
    return render(request, "producto/unidades/listar.html", context)

@login_required
def unidades_modificar(request, pk):
    titulo = "Unidades"
    unidades = Unidades.objects.get(id=pk)

    if request.method == "POST":
        form = UnidadesUpdateForm(request.POST, instance=unidades)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("unidades")
    else:
        form = UnidadesUpdateForm(instance=unidades)
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/unidades/modificar.html", context)

@login_required
def unidades_eliminar(request, pk):
    unidades = Unidades.objects.filter(id=pk)
    unidades.update(estado="0")
    return redirect("unidades")

@login_required
def subcategoria_crear(request):
    titulo = "Subcategoría"
    if request.method == "POST":
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("producto")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = SubcategoriaForm()
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/subcategoria/crear.html", context)

@login_required
def subcategoria_listar(request):
    titulo = "Subcategoría"
    modulo = "Producto"
    subcategorias = Subcategoria.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "subcategorias": subcategorias, "user":request.user}
    return render(request, "producto/subcategoria/listar.html", context)

@login_required
def subcategoria_modificar(request, pk):
    titulo = "Subcategoría"
    subcategoria = Subcategoria.objects.get(id=pk)

    if request.method == "POST":
        form = SubcategoriaUpdateForm(request.POST, instance=subcategoria)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("subcategoria")
    else:
        form = SubcategoriaUpdateForm(instance=subcategoria)
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/subcategoria/modificar.html", context)

@login_required
def subcategoria_eliminar(request, pk):
    subcategoria = Subcategoria.objects.filter(id=pk)
    subcategoria.update(estado="0")
    return redirect("subcategoria")

@login_required
def categoria_crear(request):
    titulo = "Categoría"
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("producto")
    else:
        form = CategoriaForm()
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/categoria/crear.html", context)

@login_required
def categoria_listar(request):
    titulo = "Categoría"
    modulo = "Producto"
    categorias = Categoria.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "categorias": categorias, "user":request.user}
    return render(request, "producto/categoria/listar.html", context)

@login_required
def categoria_modificar(request, pk):
    titulo = "Categoría"
    categoria = Categoria.objects.get(id=pk)

    if request.method == "POST":
        form = CategoriaUpdateForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("categoria")
    else:
        form = CategoriaUpdateForm(instance=categoria)
        subcategoria_activos = Subcategoria.objects.filter(estado='1')
        form.fields['subcategoria'].queryset = subcategoria_activos
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "producto/categoria/modificar.html", context)

@login_required
def categoria_eliminar(request, pk):
    categoria = Categoria.objects.filter(id=pk)
    categoria.update(estado="0")
    return redirect("categoria")
