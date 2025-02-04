from django.urls import path
from apps.livros.views import (
    ListarLivrosView,
    AdicionarLivroView,
    DetalhesLivroView,
    FavoritarLivroView,
    DesfavoritarLivroView,
)

app_name = 'livros'

urlpatterns = [
    path('livros/', ListarLivrosView.as_view(), name='lista_livros'),
    path('livros/<slug:slug>', DetalhesLivroView.as_view(), name='detalhes_livro'),
    path('livros/adicionar/', AdicionarLivroView.as_view(), name='novo_livro'),
    path('livros/<slug:slug>favoritar/', FavoritarLivroView.as_view(), name='favoritar_livro'),
    path('livros/<slug:slug>/desfavoritar/', DesfavoritarLivroView.as_view(), name='desfavoritar_livro'),
]
