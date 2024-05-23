from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm, CustomUserChangeForm, PropiedadForm, CrearForm
from .models import Propiedad, Comuna
from django.core.paginator import Paginator
from django.contrib import messages


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
            return redirect('login')
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
    


@login_required
def mis_propiedades(request):
    # Filtrar las propiedades del usuario actualmente autenticado
    propiedades_usuario = Propiedad.objects.filter(propietario=request.user)

    # Obtener el tipo de filtro actual
    tipo_filtro = request.GET.get('tipo', None)

    # Aplicar el filtro por tipo si está presente
    if tipo_filtro:
        # Filtrar por el tipo de inmueble seleccionado
        propiedades_usuario = propiedades_usuario.filter(tipo_inmueble=tipo_filtro)

    # Paginar los resultados
    paginator = Paginator(propiedades_usuario, 6)  # Muestra 6 propiedades por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'registration/mis_propiedades.html', {'page_obj': page_obj, 'tipo_filtro': tipo_filtro})

##################

""" @login_required
def editar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id, propietario=request.user)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('mis_propiedades')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'editar_propiedad.html', {'form': form, 'propiedad': propiedad}) """

@login_required
def editar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id, propietario=request.user)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            form.save()
            messages.success(request, 'La propiedad se editó correctamente.')
            return redirect('mis_propiedades')
        else:
            messages.error(request, 'Hubo un error al editar la propiedad. Por favor, corrija los errores.')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'registration/editar_propiedad.html', {'form': form, 'propiedad': propiedad})

##################


@login_required
def eliminar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id, propietario=request.user)

    if request.method == 'POST':
        propiedad.delete()
        messages.success(request, 'La propiedad se eliminó correctamente.')
        return redirect('mis_propiedades')
    else:
        return redirect('mis_propiedades')


@login_required
def crear_propiedad(request):
    if request.method == 'POST':
        form = CrearForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige a la página de inicio después de guardar la vivienda
    else:
        form = CrearForm()
    return render(request, 'registration/crear_propiedad.html', {'form': form})

