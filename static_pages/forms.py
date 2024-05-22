from django import forms
from django.contrib.auth.models import User

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

