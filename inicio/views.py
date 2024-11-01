from django.shortcuts import render, redirect
from datetime import datetime
from django.template import loader
from inicio.models import Producto
from inicio.forms import Productoform
from django.contrib.auth.decorators import login_required
 
def inicio (request,):
    fecha_actual = datetime.now()
    datos = {'fecha_actual' : fecha_actual}
    return render(request, 'inicio.html', datos)

def acerca(request):
    return render(request, 'acerca.html')


def agregar_producto_view(request):
    
    if not request.user.is_authenticated:
        return redirect('usuarios:login')
    
    if request.method == 'POST':
        form = Productoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ver_pedido')  
    else:
        form = Productoform()
    return render(request, 'agregar_producto.html', {'form': form})


def ver_pedido_view(request):
    productos = Producto.objects.all()
    
    return render(request, 'ver_producto.html', {'productos': productos})

def eliminar_producto(request, id):
    productos = Producto.objects.get(id=id)
    productos.delete()
    return redirect('inicio:agregar_producto')

 
    