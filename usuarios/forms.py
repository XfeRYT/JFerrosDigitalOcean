from django import forms
from django.forms import ModelForm, widgets
from usuarios.models import Usuario
from usuarios.models import Sucursal
class SucursalForm(forms.ModelForm):
    class Meta:
        model=Sucursal
        fields = "__all__"
        exclude=["estado"]
class SucursalUpdateForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = "__all__"
        exclude=["estado"]

        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields = "__all__"
        exclude=["estado","user"]

class UsuarioUpdateForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["estado","documento","tipo_documento","rol","user"]
