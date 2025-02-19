# Importação da interface de administração fornecida pelo Django
from django.contrib import admin
# Modelos para configurar a tela de administrador
from .models import Link, Livros, Comentario, Editora

# Registração do modelo 'Editora' na tela de admin
@admin.register(Editora)
# Definição da classe 'EditoraAdmin' que herda de uma classe padrão do Django
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',) # Atributo que aparecerá na lista

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('site', 'link',)
    search_fields = ('site',)

@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_publicacao', 'editora', 'autor')
    list_filter = ('ano_publicacao', 'editora',)
    search_fields = ('titulo', 'autor__nome', 'editora')
    autocomplete_fields = ('autor', 'materia') # Atributos em caixas de pesquisas com autocomplete

@admin.register(Comentario)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'postado_em')
    list_filter = ('postado_em',)
    search_fields = ('livro', 'usuario', 'postado_em')
    autocomplete_fields = ('livro', 'usuario') # Atributos em caixas de pesquisas com autocomplete
