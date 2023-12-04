from django.shortcuts import render, redirect
from usuarios.models import Usuario
from producto.models import Producto
from compras.models import Compra
from compras.forms import CompraForm, CompraUpdateForm
from compras.models import Cuenta_Pendiente
from compras.forms import Cuenta_PendienteForm, Cuenta_PendienteUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def compra_crear(request):
    titulo = "Compra"
    form = CompraForm(request.POST)
    if form.is_valid():
        compra = form.save(commit=False)
        usuarios = Usuario.objects.filter(documento=request.user)
        if usuarios.exists():
            usuario = usuarios.first()  # You may want to implement a more sophisticated logic here
            compra.usuario = usuario
            compra.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("detalle_compra", compra.id)
        else:
            messages.error(request, "No se encontró ningún usuario con el documento proporcionado.")
    else:
        messages.error(request, "El formulario tiene errores.")


    context = {"titulo": titulo, "form": form, "user":request.user}
    return redirect("compra")



@login_required
def compra_listar(request):
    titulo = "Compra"
    modulo = "Compras"
    compras = Compra.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "compras": compras, "user":request.user}
    return render(request, "compras/compras/listar.html", context)

@login_required
def compra_modificar(request, pk):
    titulo = "Compra"
    compra = Compra.objects.get(id=pk)

    if request.method == "POST":
        form = CompraUpdateForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("compra")
        else:
            messages.success(request, "El formulario se ha modificado correctamente.")
    else:
        form = CompraUpdateForm(instance=compra)
        usuarios_activos = Usuario.objects.filter(estado='1')
        form.fields['idusuario'].queryset = usuarios_activos
        cuenta_pendiente_activos = Cuenta_Pendiente.objects.filter(estado='1')
        form.fields['idcuentapendiente'].queryset = cuenta_pendiente_activos
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "compras/compras/modificar.html", context)

@login_required
def compra_eliminar(request, pk):
    compra = Compra.objects.filter(id=pk)
    compra.delete()
    return redirect("compra")

@login_required
def cuenta_pendiente_crear(request):
    titulo = "Cuenta Pendiente"
    if request.method == "POST":
        form = Cuenta_PendienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("compra")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Cuenta_PendienteForm()
        productos_activos = Producto.objects.filter(estado='1')
        form.fields['nombre_producto'].queryset = productos_activos
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "compras/cuentaspendientes/crear.html", context)

@login_required
def cuenta_pendiente_listar(request):
    titulo = "Cuenta Pendiente"
    modulo = "Compras"
    cuentaspendientes = Cuenta_Pendiente.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "cuentaspendientes": cuentaspendientes,
        "user":request.user
    }
    return render(request, "compras/cuentaspendientes/listar.html", context)

@login_required
def cuenta_pendiente_modificar(request, pk):
    titulo = "Cuenta Pendiente"
    cuentapendiente = Cuenta_Pendiente.objects.get(id=pk)

    if request.method == "POST":
        form = Cuenta_PendienteUpdateForm(request.POST, instance=cuentapendiente)
        if form.is_valid():
            # Obtén el valor actual y el valor a restar desde el formulario
            valor_actual = cuentapendiente.valor
            valor_restar = form.cleaned_data['valor_restar']

            # Verifica que el valor a restar no sea mayor que el valor actual
            if valor_restar > valor_actual:
                form.add_error('valor_restar', 'El valor a restar no puede ser mayor que el saldo pendiente.')
            else:
                # Realiza la resta solo si la validación pasa
                instance = form.save(commit=False)
                instance.valor = valor_actual - valor_restar
                instance.save()

                messages.success(request, "El formulario se ha modificado correctamente.")
                return redirect("cuenta_pendiente")
    else:
        form = Cuenta_PendienteUpdateForm(instance=cuentapendiente)

    context = {"titulo": titulo, "form": form, "user": request.user}
    return render(request, "compras/cuentaspendientes/modificar.html", context)
@login_required
def cuenta_pendiente_eliminar(request, pk):
    cuentapendiente = Cuenta_Pendiente.objects.filter(id=pk)
    cuentapendiente.update(estado="0")
    return redirect("cuenta_pendiente")
