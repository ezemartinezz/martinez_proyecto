from django.urls import path
from inicio.views import inicio, primer_template

urlpatterns = [
     path('', inicio),
     path('primer-template/', primer_template),
]