from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.usuario.views import (
    HomePage, 
    RegistrarUsuarioView, 
    LoginUsuarioView,
    PerfilUsuarioView,
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('perfil/<username>', PerfilUsuarioView.as_view(), name='perfil'),
]