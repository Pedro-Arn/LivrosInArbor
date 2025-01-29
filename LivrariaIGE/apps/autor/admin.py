from django.contrib import admin
from .models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'data_nascimento')
    search_fields = ('nome_completo',)
    ordering = ('nome_completo',)
    list_filter = ('data_nascimento',)
