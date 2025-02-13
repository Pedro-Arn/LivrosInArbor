from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.usuario.models import Usuario, Favoritos


class RegistrarUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'E-mail',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Insira a senha',
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


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['foto_perfil', 'first_name', 'data_nascimento']


class GerenciarFavoritosForm(forms.Form):
    favoritos = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def __init__(self, usuario, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['favoritos'].queryset = Favoritos.objects.filter(usuario=usuario).select_related('livro')

    def save(self):
        favoritos_to_delete = self.cleaned_data['favoritos']
        favoritos_to_delete.delete()