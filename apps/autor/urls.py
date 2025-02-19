# Importação de uma função Django que associa URL'S
from django.urls import path
# Importação da classe 'DetalhesAutorView'
from apps.autor.views import DetalhesAutorView

app_name = 'autor'

# Definição da URL para o app 'autor'
urlpatterns = [
    path('autor/<slug:slug>', DetalhesAutorView.as_view(), name='detalhes_autor'),
]