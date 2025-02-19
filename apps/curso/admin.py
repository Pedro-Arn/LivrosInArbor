# Importação da interface de administração fornecida pelo Django
from django.contrib import admin
# Modelos para configurar a tela de administrador
from .models import Materias, Cursos

# Registração do modelo 'Materias' na tela de admin
@admin.register(Materias)
# Definição da classe 'MateriasAdmin' que herda de uma classe padrão do Django
class MateriasAdmin(admin.ModelAdmin):
    # Todos os elementos e funcionalidades que constaram na interface
    list_display = ('nome', 'fase_basica', 'periodo') # Atributos que aparecerão na lista
    list_filter = ('fase_basica', 'periodo') # Atributos que servirão como filtro
    search_fields = ('nome',) # Atributo que poderá ser pesquisado
    ordering = ('periodo', 'nome') # Atributos que servirão como ordenação

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    filter_horizontal = ('materias',)  # Facilita a seleção de matérias na tela admin
    ordering = ('nome',)