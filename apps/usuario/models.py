from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from apps.usuario.choices import (
    Generos,
    Ocupacoes,
    Identificacoes,
)


def validate_identificacao(value):
    if not str(value).isdigit():  # Ensure it's a numeric value
        raise ValidationError("Identification must be numeric.")
    if len(str(value)) < 11 or len(str(value)) > 13:
        raise ValidationError("Identification must be between 11 and 13 digits.")

class Usuario(User):
    ocupacao = models.CharField(
        # verbose_name='Ocupação',
        max_length=1,
        choices=Ocupacoes.choices,
        null=False,
        blank=False,
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de nascimento",
    )
    tipo_identificacao = models.CharField(
        max_length=1,
        choices=Identificacoes.choices,
        default='C',
    )
    identificacao = models.CharField(
        max_length=13,
        unique=True,
        null=False,
        blank=True,
        validators=[validate_identificacao],
    )
    genero = models.CharField(
        max_length=1,
        choices=Generos.choices,
        blank=False,
        null=False,
    )

