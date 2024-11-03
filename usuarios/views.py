from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioCreacionUsuario,  FormularioEdicionPerfil
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra


def login(request):
    
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            mail = formulario.cleaned_data.get('email')
            contraseña= formulario.cleaned_data.get('password')
            
            usuario = authenticate(username = nombre_usuario, password= contraseña)
        
            django_login(request, usuario)
            
            objeto_creado, booleano_si_se_creo_o_no = DatosExtra.objects.get_or_create(user= usuario)
            
            return redirect('inicio')
            
    return render(request, 'usuarios/login.html', {'form': formulario })

def registrarse(request):
    
    formulario = FormularioCreacionUsuario()
    if request.method == 'POST':
        formulario = FormularioCreacionUsuario(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            
            return redirect('usuarios:login')
            
    return render(request, 'usuarios/registrarse.html', {'form': formulario})


def ver_usuario(request):
    datos_extra = request.user.datosextra
    return render(request, 'usuarios/ver_usuario.html', {'user': request.user, 'datos_extra': datos_extra})

def editar_perfil(request):
    datos_extra = request.user.datosextra
    formulario = FormularioEdicionPerfil(instance=request.user)

    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            formulario.save()
            
            new_avatar = request.FILES.get('avatar')
            if new_avatar:
                datos_extra.avatar = new_avatar
            
            datos_extra.save()

            return redirect('inicio')  
               
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario, 'datos_extra': datos_extra})


class CambiarContraseña(LoginRequiredMixin,PasswordChangeView):
    template_name = 'usuarios/cambiar_contraseña.html'
    success_url = reverse_lazy('usuarios:editar_perfil')
    
    
