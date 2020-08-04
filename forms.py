from django import forms
from .models import Productos, Cuadernos, Lapices, Mochilas, Juguetes, Piñateria, Obsequios

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
class JuguetesForm(forms.ModelForm):
    class Meta:
        model = Juguetes
        fields = '__all__'
class PiñateriaForm(forms.ModelForm):
    class Meta:
        model = Piñateria
        fields = '__all__'
class ObsequiosForm(forms.ModelForm):
    class Meta:
        model = Obsequios
        fields = '__all__'