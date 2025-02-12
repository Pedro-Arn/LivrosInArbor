from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget

from apps.livros.models import Livros, Comentario

class FiltrarLivrosForm(forms.Form):
    class Meta:
        model = Livros
        fields = ['ano_publicação', 'editora', 'materia',]

class AdicionarLivrosForm(forms.ModelForm):
    new_links = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Insira os links no formato: Nome do site,URL\nNome do site,URL.'}),
        required=False,
        help_text='Insira os links no formato: Nome do site,URL (um por linha)..'
    )

    class Meta:
        model = Livros
        fields = '__all__' 
        exclude = ['slug', 'links']
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
        fields = ['corpo']

        widgets = {
            'corpo': forms.Textarea(attrs={
                'placeholder': 'Digite seu comentário aqui...',
                'class': 'textarea-comentario',
                'rows': 4,
                'cols': 50, 
            })
        }
