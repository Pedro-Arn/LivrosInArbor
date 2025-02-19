# Importação da interface de administração fornecida pelo Django
from django.contrib import admin
# Importação da funções para criar rotas de URL
from django.urls import path, include, re_path
# Importações para configurar a exibição de estáticos e de mídia
from django.conf import settings
from django.conf.urls.static import static

# Lista onde as URLs e suas visualizações são associadas
urlpatterns = [
    path("admin/", admin.site.urls),
    re_path('', include('apps.autor.urls')),
    re_path('', include('apps.livros.urls')),
    re_path('', include('apps.usuario.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)