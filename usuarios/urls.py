from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('perfil/editar/', views.editar_perfil, name = 'editar_perfil'),
    path('perfil/editar/contraseña/', views.CambiarContraseña.as_view(), name = 'cambiar_contraseña'),
    path('logout/', LogoutView.as_view(template_name= 'usuarios/logout.html'), name='logout'),
    
] 
