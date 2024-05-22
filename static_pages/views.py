from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
from .models import Propiedad  
from django.core.paginator import Paginator
from .forms import CustomUserChangeForm 

def index(request):
    # Obtener todos los objetos de Propiedad
    propiedades = Propiedad.objects.all()

    # Verificar si se está aplicando un filtro por tipo
    tipo_filtro = request.GET.get('tipo', None)
    if tipo_filtro:
        # Filtrar por el tipo de inmueble seleccionado
        propiedades = propiedades.filter(tipo_inmueble=tipo_filtro)

    # Paginar los resultados
    paginator = Paginator(propiedades, 6)  # Muestra 6 propiedades por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj, 'tipo_filtro': tipo_filtro})


@login_required
def secreto(request):
    return render(request, 'secreto.html')



def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Para poder guardar la contraseña de forma encriptada
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('secreto')
    else:
        form = UserForm()

    return render(request, 'registration/registro.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = '/'

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')  # Cambia 'inicio' por el nombre de la URL de la página principal
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')  # Cambia 'inicio' por el nombre de la URL de la página principal



def catalogo(request):
    # Obtener todos los objetos de Propiedad
    propiedades = Propiedad.objects.all()

    # Verificar si se está aplicando un filtro por tipo
    tipo_filtro = request.GET.get('tipo', None)
    if tipo_filtro:
        # Filtrar por el tipo de inmueble seleccionado
        propiedades = propiedades.filter(tipo_inmueble=tipo_filtro)

    # Paginar los resultados
    paginator = Paginator(propiedades, 6)  # Muestra 6 propiedades por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalogo.html', {'page_obj': page_obj, 'tipo_filtro': tipo_filtro})


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'registration/editar_perfil.html', {'form': form})
