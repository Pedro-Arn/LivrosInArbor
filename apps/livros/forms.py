from django import forms

from apps.livros.models import Livros, Comentario

class FiltrarLivrosForm(forms.Form):
    class Meta:
        model = Livros
        fields = ['ano_publicação', 'editora', 'materia',]

class AdicionarLivrosForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__' 

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
