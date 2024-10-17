from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length= 20)
    categoria = models.CharField(max_length= 20)
    descripcion = models.TextField(max_length= 20)
    
