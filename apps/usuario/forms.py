from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.usuario.models import Usuario


class RegistrarUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'E-mail',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme a senha',
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme a senha',
        }),
    )

    class Meta:
        model = Usuario
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'ocupacao',
            'data_nascimento',
            'tipo_identificacao',
            'identificacao',
            'genero',
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Usuário',
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Nome',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Sobrenome',
            }),
            'ocupacao': forms.Select(attrs={
            }),
            'data_nascimento': forms.DateInput(attrs={
                'type': 'date',
            }),
            'identificacao': forms.TextInput(attrs={
                'placeholder': 'Número de Identificação',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Senha',
            }),
        }