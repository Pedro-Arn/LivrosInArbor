# Importação de uma classe do Django que exibe detalhes
from django.views.generic import (
    DetailView,
)
# Importação da classe 'Autor' e seu app
from apps.autor.models import Autor

# Criação da classe 'DetalhesAutorView' que faz a chamada do modelo e da tela correspondente a ela
class DetalhesAutorView(DetailView):
    model = Autor
    template_name = 'autor.html'
