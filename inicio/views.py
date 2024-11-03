from django.shortcuts import render, redirect,get_object_or_404
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
        form = Productoform(request.POST, request.FILES)
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
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('/ver_pedido')  # Reemplaza con el nombre de tu vista



    