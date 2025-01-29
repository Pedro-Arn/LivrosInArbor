from django.contrib import admin
from .models import Materias, Cursos

@admin.register(Materias)
class MateriasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fase_basica', 'periodo')
    list_filter = ('fase_basica', 'periodo')
    search_fields = ('nome',)
    ordering = ('periodo', 'nome')

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    filter_horizontal = ('materias',)  # Facilita a seleção de matérias no admin
    ordering = ('nome',)
