from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Propiedad


class UserForm(forms.ModelForm):
    ROLES = [
        ('arrendador', 'Arrendador'),
        ('arrendatario', 'Arrendatario'),
    ]
    role = forms.ChoiceField(choices=ROLES, label="Rol")
    email = forms.EmailField(max_length=200, help_text='Required', label="Email")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label="Contraseña")
    is_staff = forms.BooleanField(label="Agregar al staff", required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_staff')
        labels = {
            'username': 'Alias',
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'






class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'estacionamientos', 
                  'habitaciones', 'banos', 'direccion', 'comuna', 'tipo_inmueble', 
                  'precio_arriendo', 'imagen']


class CrearForm(forms.ModelForm):
    class Meta:
        model = Propiedad  # Cambia 'CrearForm' por el nombre correcto de tu modelo
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'estacionamientos', 
                  'habitaciones', 'banos', 'direccion', 'comuna', 'tipo_inmueble', 
                  'precio_arriendo', 'imagen']