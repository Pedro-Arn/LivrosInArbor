from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.usuario.views import (
    HomePage, 
    RegistrarUsuarioView, 
    PerfilUsuarioView,
)

app_name = 'usuario'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', RegistrarUsuarioView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='usuario:home'), name='logout'),
    path('perfil/<username>', PerfilUsuarioView.as_view(), name='perfil'),
]