# Importação do módulo de crição de formulários
from django import forms
# Importação da classe com formulário padrão para a criação de novos usuários
from django.contrib.auth.forms import UserCreationForm
# Importação de classes de associação
from apps.usuario.models import Usuario, Favoritos

# Definição de formulário para registrar usuarios
class RegistrarUsuarioForm(UserCreationForm):
    email = forms.EmailField( # Tipo campo e-mail válido
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'E-mail',
        })
    )
    password1 = forms.CharField( # Tipo campo livre
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Insira a senha',
        }),
    )
    password2 = forms.CharField( # Tipo campo livre
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme a senha',
        }),
    )

    # Configuração de informações adicionais
    class Meta:
        model = Usuario
        fields = ( # Inclui alguns campos de usuario
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

        # Definição dos widgets personalizados para os campos do formulário
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

# Classe de Formulário para Editar Perfil
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['foto_perfil', 'first_name', 'data_nascimento']

# Classe de Formulário para Gerenciar Favoritos do Usuário
class GerenciarFavoritosForm(forms.Form):
    favoritos = forms.ModelMultipleChoiceField(
        queryset=None, # Não é uma lista definida quando instanciada
        widget=forms.CheckboxSelectMultiple, # Exibe uma lista de caixas de seleção
        required=False, # Não obrigatório
    )
    
    # Traz apenas os favoritos associados ao usuário correspondente
    def __init__(self, usuario, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['favoritos'].queryset = Favoritos.objects.filter(usuario=usuario).select_related('livro')

    # Exclui os favoritos selecionados pelo usuário
    def save(self):
        favoritos_to_delete = self.cleaned_data['favoritos']
        favoritos_to_delete.delete()