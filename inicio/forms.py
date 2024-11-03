from django import forms
from .models import Producto

class Productoform(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'imagen']
        
class FormularioEdicionProducto(Productoform):
    nombre = forms.CharField(label= 'Nombre')
    categoria = forms.CharField(label= 'Apellido')
    descripcion = forms.CharField()
    imagen = forms.ImageField(required=False)