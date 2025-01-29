from django.urls import path

from apps.autor.views import DetalhesAutorView

urlpatterns = [
    path('autor/<slug:slug>', DetalhesAutorView.as_view(), name='detalhes_autor'),
]