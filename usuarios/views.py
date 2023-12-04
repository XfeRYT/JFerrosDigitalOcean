from django.shortcuts import render, redirect
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm, UsuarioUpdateForm
from usuarios.models import Sucursal
from usuarios.forms import SucursalForm, SucursalUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
def usuario_crear(request):
    """
    Vista para la creación de un nuevo usuario.
    """
    titulo = "Usuario"
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Genera una contraseña basada en algunos datos del formulario
            primer_nombre = form.cleaned_data['nombre'][0].upper()
            primer_apellido = form.cleaned_data['apellido'][0].lower()
            ultimos_digitos_documento = form.cleaned_data['documento'][-4:]
            nueva_contrasena = f"@{primer_nombre}{primer_apellido}{ultimos_digitos_documento}"
            
            # Encripta la contraseña
            contrasena_encriptada = make_password(nueva_contrasena)
            
            # Crea un nuevo usuario de Django
            nuevo_usuario = User(
                username=form.cleaned_data['documento'],  # Reemplaza con el campo correcto del formulario
                password=contrasena_encriptada,  # Reemplaza con el campo correcto del formulario
                email=form.cleaned_data['correo'],
                first_name=form.cleaned_data['nombre'],  # Campo de nombre
                last_name=form.cleaned_data['apellido'],  # Campo de apellido
                # Agrega otros campos de usuario de Django según sea necesario
                # Por ejemplo, puedes agregar más campos como date_of_birth, is_active, etc.
            )
            nuevo_usuario.save()
            
            # Guarda el usuario personalizado asociado
            usuario = form.save(commit=False)
            usuario.usuario = nuevo_usuario
            usuario.save()
            
            # Asigna el usuario al grupo seleccionado
            grupo_seleccionado = form.cleaned_data['rol']
            nuevo_usuario.groups.add(grupo_seleccionado)
            
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("usuario")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = UsuarioForm()
    
    context = {"titulo": titulo, "form": form, "user": request.user}
    return render(request, "usuarios/usuarios/crear.html", context)

@login_required
def usuario_listar(request):
    """
    Vista para listar todos los usuarios.
    """
    titulo = "Usuario"
    modulo = "Usuarios"
    usuarios = Usuario.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "usuarios": usuarios, "user": request.user}
    return render(request, "usuarios/usuarios/listar.html", context)

@login_required
def usuario_modificar(request, pk):
    """
    Vista para modificar un usuario existente.
    """
    titulo = "Usuario"
    usuario = Usuario.objects.get(id=pk)

    if request.method == "POST":
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("usuario")
    else:
        form = UsuarioUpdateForm(instance=usuario)
    
    context = {"titulo": titulo, "form": form, "user": request.user}
    return render(request, "usuarios/usuarios/modificar.html", context)

@login_required
def usuario_eliminar(request, pk):
    """
    Vista para eliminar un usuario.
    """
    usuario = Usuario.objects.filter(id=pk)
    usuario.update(estado="0")
    return redirect("usuario")


@login_required
def sucursal_crear(request):
    titulo = "Sucursal"
    if request.method == "POST":
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("usuario")
    else:
        form = SucursalForm()
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "usuarios/sucursal/crear.html", context)

@login_required
def sucursal_listar(request):
    titulo = "Sucursal"
    modulo = "Usuarios"
    sucursales = Sucursal.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "sucursales": sucursales, "user":request.user}
    return render(request, "usuarios/sucursal/listar.html", context)

@login_required
def sucursal_modificar(request, pk):
    titulo = "Sucursal"
    sucursal = Sucursal.objects.get(id=pk)

    if request.method == "POST":
        form = SucursalUpdateForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("sucursal")
    else:
        form = SucursalUpdateForm(instance=sucursal)
    context = {"titulo": titulo, "form": form, "user":request.user}
    return render(request, "usuarios/sucursal/modificar.html", context)

@login_required
def sucursal_eliminar(request, pk):
    sucursal = Sucursal.objects.filter(id=pk)
    sucursal.update(estado="0")
    return redirect("sucursal")
