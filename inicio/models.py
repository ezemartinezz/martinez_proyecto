from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length= 200)
    categoria = models.CharField(max_length= 200)
    descripcion = models.TextField(max_length= 1000)
    imagen =  models.ImageField(upload_to='product_pics/', null=True, blank=True)  # Permitir null y vacío


