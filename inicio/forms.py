from django import forms
from .models import Producto

class Productoform(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'imagen']