from django import forms
from .models import Productos, Cuadernos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

class CuadernosForm(forms.ModelForm):
    class Meta:
        model = Cuadernos
        fields = '__all__'
