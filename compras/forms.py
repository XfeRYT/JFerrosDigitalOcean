from django import forms
from django.forms import ModelForm, widgets
from compras.models import Compra
from compras.models import Cuenta_Pendiente

class CompraForm(forms.ModelForm):
    class Meta:
        model=Compra
        fields = "__all__"
        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
        exclude=["estado","fecha","usuario"]
class CompraUpdateForm(ModelForm):
    class Meta:
        model = Compra
        fields = "__all__"
        exclude=["estado","fecha"]
        
class Cuenta_PendienteForm(forms.ModelForm):
    class Meta:
        model=Cuenta_Pendiente
        fields = "__all__"
        widgets={
            'fecha_inicio': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
        exclude=["fecha_inicio","estado","valor_restar"]
class Cuenta_PendienteUpdateForm(ModelForm):
    class Meta:
        model = Cuenta_Pendiente
        fields = "__all__"
        exclude=["fecha_inicio","estado","nombre","nombre_producto","valor"]
