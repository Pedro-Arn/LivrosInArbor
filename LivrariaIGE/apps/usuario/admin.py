from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'ocupacao', 'data_nascimento', 'genero')
    search_fields = ('username', 'first_name', 'email', 'identificacao')
    list_filter = ('ocupacao', 'genero')
    ordering = ('first_name',)
