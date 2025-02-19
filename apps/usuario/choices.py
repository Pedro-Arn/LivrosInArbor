# Importação do módulo models do Django
from django.db import models

# Definição de uma classe enumerada 'Generos'
class Generos(models.TextChoices):
    # Valores para armazenamento no BD e para exibição
    MASCULINO = 'M', 'Masculino' 
    FEMININO = 'F', 'Feminino'
    OUTRO = 'O', 'Outro'

# Definição de uma classe enumerada 'Ocupacoes'
class Ocupacoes(models.TextChoices):
    ESTUDANTE = 'E', 'Estudante'
    PROFESSOR = 'P', 'Professor'
    OUTRO = 'V', 'Visitante'

# Definição de uma classe enumerada 'Identificacoes'
class Identificacoes(models.TextChoices):
    MATRICULA = 'M', 'Matrícula'
    CPF = 'C', 'CPF'
