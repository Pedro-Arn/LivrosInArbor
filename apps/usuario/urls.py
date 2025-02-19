# Importação de uma função Django que associa URL'S
from django.urls import path
# Importação de uma view do Djando para permitir o logout
from django.contrib.auth.views import LogoutView
# Importação das classes de interesse ao usuario
from apps.usuario.views import (
    HomePage, 
    RegistrarUsuarioView, 
    PerfilUsuarioView,
)

app_name = 'usuario'

 # Definição da URL para o app 'usuario'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', RegistrarUsuarioView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='usuario:home'), name='logout'),
    path('perfil/<username>', PerfilUsuarioView.as_view(), name='perfil'),
]