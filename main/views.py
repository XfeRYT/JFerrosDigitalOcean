from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def principal(request):
    titulo="Bienvenido a JFerros"
    context={
        "titulo":titulo,
    }
    return render(request, "index.html",context)
@login_required
def logout_user(request):
    logout(request)
    return redirect('inicio')
@login_required
def body_productos(request):
    titulo="Bienvenido"
    context={
        "titulo":titulo,
    }
    return render(request, "partials/body-productos.html",context)
@login_required
def body_produ_vestuario(request):
    titulo="Bienvenido"
    context={
        "titulo":titulo,
    }
    return render(request, "partials/body-produ-vestuarios.html",context)
@login_required
def body_produ_electricidad(request):
    titulo="Bienvenido"
    context={
        "titulo":titulo,
    }
    return render(request, "partials/body-produ-electricidad.html",context)
@login_required
def body_produ_fontaneria(request):
    titulo="Bienvenido"
    context={
        "titulo":titulo,
    }
    return render(request, "partials/body-produ-fontaneria.html",context)
@login_required
def body_produ_sellantes(request):
    titulo="Bienvenido"
    context={
        "titulo":titulo,
    }
    return render(request, "partials/body-produ-sellantes.html",context)
@login_required
def body_produ_pinturas(request):
    titulo="Bienvenido"
    context={
        "titulo":titulo,
    }
    return render(request, "partials/body-produ-pinturas.html",context)


