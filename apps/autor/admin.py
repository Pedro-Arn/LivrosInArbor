# Importação da interface de administração fornecida pelo Django
from django.contrib import admin
# Modelo para configurar a tela de administrador
from .models import Autor

# Registração do modelo 'Autor' na tela de admin
@admin.register(Autor)
# Definição da classe 'AutorAdmin' que herda de uma classe padrão do Django
class AutorAdmin(admin.ModelAdmin):
    # Todos os elementos e funcionalidades que constaram na interface
    list_display = ('nome_completo', 'data_nascimento') # Atributos que aparecerão na lista
    search_fields = ('nome_completo',) # Atributo que poderá ser pesquisado
    ordering = ('nome_completo',) # Atributo que servirá como ordenação
    list_filter = ('data_nascimento',) # Atributo que servirá como filtro
