from django import forms
from django.forms import ModelForm, widgets
from producto.models import Marca
from producto.models import Producto
from producto.models import Unidades
from producto.models import Subcategoria
from producto.models import Categoria



class ProductoForm(forms.ModelForm):
    precio_str = forms.CharField(label="Precio Unitario", max_length=20)
    class Meta:
        model=Producto
        fields = "__all__"
        exclude=["estado", 'precio']
        
    def clean_precio_str(self):
        precio_str = self.cleaned_data['precio_str']
        precio_str = precio_str.replace(",", "").replace(".", "")  # Remover comas y puntos
        try:
            precio_decimal = float(precio_str)
            return precio_decimal
        except ValueError:
            raise forms.ValidationError("Asegúrese de ingresar un valor numérico válido.")
        try:
            precio_decimal = round(float(precio_str.replace(",", "").replace(".", "").replace(" ", "")), 2)
            if precio_decimal < 0:
                raise ValidationError("El precio debe ser mayor o igual a cero.")
            return precio_decimal
        except (ValueError, TypeError):
            raise ValidationError("Asegúrese de ingresar un valor numérico válido.")
        main

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            self.add_error('stock', "El valor del stock debe ser un número positivo.")
        return stock
class ProductoUpdateForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        exclude=["estado"]
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = "__all__"
        exclude=["estado"]
class MarcaUpdateForm(ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"
        exclude=["estado"]

class UnidadesForm(forms.ModelForm):
    class Meta:
        model=Unidades
        fields = "__all__"
        exclude=["estado"]
        
class UnidadesUpdateForm(ModelForm):
    class Meta:
        model = Unidades
        fields = "__all__"
        exclude=["estado"]

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model=Subcategoria
        fields = "__all__"
        exclude=["estado"]
class SubcategoriaUpdateForm(ModelForm):
    class Meta:
        model = Subcategoria
        fields = "__all__"
        exclude=["estado"]
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = "__all__"
        exclude=["estado"]
class CategoriaUpdateForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
        exclude=["estado"]
        
