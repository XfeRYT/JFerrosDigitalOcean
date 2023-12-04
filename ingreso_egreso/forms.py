from django import forms
from django.forms import ModelForm, widgets
from ingreso_egreso.models import Detalle_Venta
from ingreso_egreso.models import Detalle_Compra
from ingreso_egreso.models import Stock
from .models import Producto


class StockForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), label="Producto")
    cantidad = forms.IntegerField(label="Cantidad")
    
class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields = "__all__"
        exclude=["estado"]
class StockUpdateForm(ModelForm):
    
    class Meta:
        model = Stock
        fields = "__all__"
        exclude=["estado"]
        
class Detalle_CompraForm(forms.ModelForm):
    class Meta:
        model=Detalle_Compra
        fields = "__all__"
        exclude=["estado","compra"]
        
class Detalle_CompraUpdateForm(ModelForm):
    
    class Meta:
        model = Detalle_Compra
        fields = "__all__"
        exclude=["estado"]
        
class Detalle_VentaForm(forms.ModelForm):
    class Meta:
        model=Detalle_Venta
        fields = "__all__"
        exclude=["estado","venta",'precio_venta']
        
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            self.add_error('stock', "El valor del stock debe ser un número positivo.")
            
class Detalle_VentaUpdateForm(ModelForm):
    
    class Meta:
        model = Detalle_Venta
        fields = "__all__"
        exclude=["estado"]