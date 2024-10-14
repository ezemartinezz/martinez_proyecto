from django.shortcuts import render
from datetime import datetime
from django.template import loader
# Create your views here.

from django.http import HttpResponse
 
def inicio (request,):
    fecha_actual = datetime.now()
    datos = {'fecha_actual' : fecha_actual}
    return render(request, 'inicio.html', datos)

def primer_template(request):
    return HttpResponse('<h3> Inciio inical </h3>')


