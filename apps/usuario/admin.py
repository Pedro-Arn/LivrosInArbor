# Importação da interface de administração fornecida pelo Django
from django.contrib import admin
# Modelo para configurar a tela de administrador
from .models import Usuario

# Registração do modelo 'Usuario' na tela de admin
@admin.register(Usuario)
# Definição da classe 'UsuarioAdmin' que herda de uma classe padrão do Django
class UsuarioAdmin(admin.ModelAdmin):
    # Todos os elementos e funcionalidades que constaram na interface
    list_display = ('username', 'first_name', 'email', 'ocupacao', 'data_nascimento', 'genero') # Atributos que aparecerão na lista
    search_fields = ('username', 'first_name', 'email', 'identificacao') # Atributos que poderão ser pesquisados
    list_filter = ('ocupacao', 'genero') # Atributos que servirão como filtros
    ordering = ('first_name',) # Atributo que servirá como ordenação
