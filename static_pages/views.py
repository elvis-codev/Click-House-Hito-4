from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
from .models import Propiedad  
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')


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
    propiedades = Propiedad.objects.all()
    paginator = Paginator(propiedades, 6)  # Muestra 6 propiedades por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogo.html', {'page_obj': page_obj})