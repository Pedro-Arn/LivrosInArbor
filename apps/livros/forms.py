# Importação do módulo de crição de formulários
from django import forms
# Importação de componentes personalisados
from django_select2.forms import Select2MultipleWidget, Select2Widget
# Importação de classes de associação
from apps.livros.models import Livros, Comentario

# Definição de formulário para adicionar livros
class AdicionarLivrosForm(forms.ModelForm):
    new_links = forms.CharField( # Tipo campo de texto longo
        widget=forms.Textarea(attrs={'placeholder': 'Insira os links no formato: Nome do site,URL\nNome do site,URL.'}),
        required=False, # É opcional
        help_text='Insira os links no formato: Nome do site,URL (um por linha)..' # Mensagem de erro
    )

    # Configuração de informações adicionais
    class Meta:
        model = Livros
        fields = '__all__' # Inclui todos os campos de livros
        exclude = ['slug', 'links'] # Exclui slug e links
        # Definição dos widgets personalizados para os campos do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição do livro',
                'rows': 4
            }),
            'ano_publicacao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'materia': Select2MultipleWidget(attrs={
                'data-placeholder': 'Selecione as matérias...',
                'data-allow-clear': 'true',
            }),
            'autor': Select2Widget(attrs={
                'data-placeholder': 'Selecione o autor...',
                'data-allow-clear': 'true',
            }),
            'editora': Select2Widget(attrs={
                'data-placeholder': 'Selecione a editora...',
                'data-allow-clear': 'true',
            }),
            'capa': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
        }

class ComentarLivroForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['corpo'] # Inclui apenas o corpo 

        widgets = {
            'corpo': forms.Textarea(attrs={
                'placeholder': 'Digite seu comentário aqui...',
                'class': 'textarea-comentario',
                'rows': 4,
                'cols': 50, 
            })
        }
