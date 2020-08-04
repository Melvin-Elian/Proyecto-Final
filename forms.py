from django import forms
from .models import Productos, Cuadernos, Lapices, Mochilas

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

class CuadernosForm(forms.ModelForm):
    class Meta:
        model = Cuadernos
        fields = '__all__'
class LapicesForm(forms.ModelForm):
    class Meta:
        model = Lapices
        fields = '__all__'
class MochilasForm(forms.ModelForm):
    class Meta:
        model = Mochilas
        fields = '__all__'