from django.views.generic import (
    DetailView,
)

from apps.autor.models import Autor

class DetalhesAutorView(DetailView):
    model = Autor
    template_name = 'autor/detalhes_autor.html'
