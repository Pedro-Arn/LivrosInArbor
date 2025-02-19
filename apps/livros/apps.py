# Importação da classe de configuração da aplicação
from django.apps import AppConfig

# Definição da classe 'LivrosConfig' que herda de uma classe padrão do Django
class LivrosConfig(AppConfig):
    # Aumentando o suporte de bits 
    default_auto_field = "django.db.models.BigAutoField"
    # Nome da aplicação
    name = "apps.livros"
