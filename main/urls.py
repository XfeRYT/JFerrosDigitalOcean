"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


from main.views import principal, logout_user, body_productos, body_produ_vestuario,body_produ_electricidad, body_produ_fontaneria, body_produ_sellantes, body_produ_pinturas
# para las iamgenes
from django.conf import settings
from django.conf.urls.static import static
# para la gestion de login y contraseña
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',auth_views.LoginView.as_view(),name='inicio'),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reiniciar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('logout/',logout_user,name="logout"),
    
    path('admin/', admin.site.urls),
    path('inicio/', principal, name="index" ),
    path('producto/', include('producto.urls') ),
    path('compras/', include('compras.urls') ),
    path('usuarios/', include('usuarios.urls') ),
    path('ingreso_egreso/', include('ingreso_egreso.urls') ),
    path('ventas/', include('ventas.urls') ),
    path('backup/', include('backup.urls') ),
        
    path('body-productos/', body_productos, name="body" ),
    path('body-produ-vestuario/', body_produ_vestuario, name="body_vestuario" ),
    path('body-produ-electricidad/', body_produ_electricidad, name="body_electricidad" ),
    path('body-produ-fontaneria/', body_produ_fontaneria, name="body_fontaneria" ),
    path('body-produ-sellantes/', body_produ_sellantes, name="body_sellantes" ),
    path('body-produ-pinturas/', body_produ_pinturas, name="body_pinturas" ),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
