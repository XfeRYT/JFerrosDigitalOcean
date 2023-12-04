from django import forms
from django.forms import ModelForm, widgets
from ventas.models import Domicilio
from ventas.models import Metododepago
from ventas.models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model=Venta
        fields = "__all__"
        exclude=["estado", "fecha","usuario"]
        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
class VentaUpdateForm(ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"
        exclude=["estado","fecha"]

class MetododepagoForm(forms.ModelForm):
    class Meta:
        model=Metododepago
        fields = "__all__"
        exclude=["estado"]
class MetododepagoUpdateForm(ModelForm):
    class Meta:
        model = Metododepago
        fields = "__all__"
        exclude=["estado"]
        
class DomicilioForm(forms.ModelForm):
    class Meta:
        model=Domicilio
        fields = "__all__"
        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_envio': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_entrega': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }        
        exclude=["estado","fecha_envio","fecha_entrega"]
class DomicilioUpdateForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = "__all__"
        widgets={
            'fecha_envio': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_entrega': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')

        }  
        exclude=["fecha","estado","usuario","direccion"]
