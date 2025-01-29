from django.db import models
from django.db.models import Q

class LivrosManager(models.Manager):
    def search_query(self, search_query):
        return self.filter(
            Q(autor__nome_completo__icontains=search_query) | \
            Q(titulo__icontains=search_query) | \
            Q(editora__icontains=search_query) | \
            Q(materia__nome__icontains=search_query)
        ).order_by('titulo')

    def filter_button(self):
        pass