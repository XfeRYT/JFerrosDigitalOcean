from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from ventas.models import Venta
from usuarios.models import Usuario
from ventas.forms import VentaForm,VentaUpdateForm
from ventas.models import Metododepago
from ventas.forms import MetododepagoForm,MetododepagoUpdateForm
from ventas.models import Domicilio
from ventas.forms import DomicilioForm,DomicilioUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def venta_crear(request):
    titulo = "Venta"
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            usuario = Usuario.objects.get(documento=request.user)
            venta.usuario = usuario
            venta.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect("detalle_venta", venta.id)
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form = VentaForm()
        metododepago_activos = Metododepago.objects.filter(estado='1')
        form.fields['metododepago'].queryset = metododepago_activos
        domicilio_activos = Domicilio.objects.filter(estado='1')
        form.fields['domicilio'].queryset = domicilio_activos
    context = {
        "titulo": titulo,
        "form": form,
        "user": request.user
    }
    return render(request, "ventas/ventas/crear.html", context)




def venta_listar(request):
    titulo="Venta"
    modulo="Ventas"
    ventas= Venta.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "ventas":ventas,
        "user":request.user
    }
    return render(request,"ventas/ventas/listar.html", context)
  
def venta_modificar(request,pk):
    titulo="Venta"
    venta= Venta.objects.get(id=pk)

    if request.method== 'POST':
        form= VentaUpdateForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('venta')
    else:
        form= VentaUpdateForm(instance=venta)
    context={
        "titulo":titulo,
        "form":form,
        "user":request.user
        }
    return render(request,"ventas/ventas/modificar.html", context)
def venta_eliminar(request,pk):
    venta= Venta.objects.filter(id=pk)
    venta.delete()
    return redirect('venta')


@login_required
def metododepago_crear(request):
    titulo="Método de pago"
    if request.method== 'POST':
        form= MetododepagoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('metododepago')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form=MetododepagoForm()
    context={
        "titulo":titulo,
        "form":form,
        "user":request.user
        }
    return render(request,"ventas/metodo_de_pago/crear.html", context)
@login_required
def metododepago_listar(request):
    titulo="Método de pago"
    modulo="Ventas"
    metodosdepagos= Metododepago.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "metodosdepagos":metodosdepagos,
        "user":request.user
    }
    return render(request,"ventas/metodo_de_pago/listar.html", context)
@login_required
def metododepago_modificar(request,pk):
    titulo="Método de pago"
    metododepago= Metododepago.objects.get(id=pk)

    if request.method== 'POST':
        form= MetododepagoUpdateForm(request.POST, instance=metododepago)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('metododepago')
    else:
        form= MetododepagoUpdateForm(instance=metododepago)
    context={
        "titulo":titulo,
        "form":form,
        "user":request.user
        }
    return render(request,"ventas/metodo_de_pago/modificar.html", context)
@login_required
def metododepago_eliminar(request,pk):
    metododepago= Metododepago.objects.filter(id=pk)
    metododepago.update(
        estado="0"
    )
    return redirect('metododepago')


@login_required
def domicilio_crear(request):
    titulo="Domicilio"
    if request.method== 'POST':
        form= DomicilioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('domicilio')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form=DomicilioForm()
        usuario_activos = Usuario.objects.filter(estado='1')
        form.fields['usuario'].queryset = usuario_activos
    context={
        "titulo":titulo,
        "form":form,
        "user":request.user
        }
    return render(request,"ventas/domicilio/crear.html", context)
@login_required
def domicilio_listar(request):
    titulo="Domicilio"
    modulo="Ventas"
    domicilios= Domicilio.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "domicilios":domicilios,
        "user":request.user
    }
    return render(request,"ventas/domicilio/listar.html", context)
@login_required
def domicilio_modificar(request,pk):
    titulo="Domicilio"
    domicilio= Domicilio.objects.get(id=pk)

    if request.method== 'POST':
        form= DomicilioUpdateForm(request.POST, instance=domicilio)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('domicilio')
    else:
        form= DomicilioUpdateForm(instance=domicilio)
    context={
        "titulo":titulo,
        "form":form,
        "user":request.user
        }
    return render(request,"ventas/domicilio/modificar.html", context)
@login_required
def domicilio_eliminar(request,pk):
    domicilio= Domicilio.objects.filter(id=pk)
    domicilio.update(
        estado="0"
    )
    return redirect('domicilio')