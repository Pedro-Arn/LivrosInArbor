# Importação de uma função Django que associa URL'S
from django.urls import path
# Importação das classes de interesse ao livro
from apps.livros.views import (
    ListarLivrosView,
    AdicionarLivroView,
    DetalhesLivroView,
    AlternarFavoritosView,
)

app_name = 'livros'

# Definição da URL para o app 'livros'
urlpatterns = [
    path('livros/', ListarLivrosView.as_view(), name='lista_livros'),
    path('livros/<slug:slug>', DetalhesLivroView.as_view(), name='detalhes_livro'),
    path('livros/adicionar/', AdicionarLivroView.as_view(), name='novo_livro'),
    path('livro/<int:pk>/favoritar/', AlternarFavoritosView.as_view(), name='alternar_favorito'),
]
