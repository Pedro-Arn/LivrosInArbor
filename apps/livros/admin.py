from django.contrib import admin
from .models import Link, Livros, Comentario, Editora


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('site', 'link',)
    search_fields = ('site',)


@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_publicacao', 'editora', 'autor')
    list_filter = ('ano_publicacao', 'editora',)
    search_fields = ('titulo', 'autor__nome', 'editora')
    autocomplete_fields = ('autor', 'materia')


@admin.register(Comentario)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'postado_em')
    list_filter = ('postado_em',)
    search_fields = ('livro', 'usuario', 'postado_em')
    autocomplete_fields = ('livro', 'usuario')
