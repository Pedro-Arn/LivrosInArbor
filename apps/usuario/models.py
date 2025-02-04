from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from apps.usuario.choices import (
    Generos,
    Ocupacoes,
    Identificacoes,
)
from apps.livros.models import Livros


# Validação do campo de identificação (numérico, 11 a 13 digitos)
def validar_identificacao(valor, tipo):
    if not valor.isdigit():  # Garante que seja um valor numerico
        raise ValidationError("Identificação deve ser um valor numérico.")
    
    comprimento = len(valor)

    if tipo == 'C' and comprimento != 11: # Validação CPF
        raise ValidationError("CPF deve ter 11 dígitos.")
    elif tipo == 'M' and comprimento != 13: # Validação matrícula
        raise ValidationError("Matrícula deve ter 13 dígitos.")


class Usuario(User):
    ocupacao = models.CharField(
        verbose_name='Ocupação',
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
    )
    genero = models.CharField(
        max_length=1,
        choices=Generos.choices,
        blank=False,
        null=False,
    )

    @property
    def nome_completo(self):
        return f"{self.first_name} {self.last_name}".strip()

    def clean(self):
        """Validação personalizada para o campo identificacao com base no tipo_identificacao."""
        super().clean()
        validar_identificacao(self.identificacao, self.tipo_identificacao)


class Favoritos(models.Model):
    livro = models.ForeignKey(
        Livros,
        related_name='livro_favorito',
        on_delete=models.CASCADE,
    )
    usuario = models.ForeignKey(
        Usuario,
        related_name='favoritos_usuario',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('livro', 'usuario')
        verbose_name = 'Livro Favorito'
        verbose_name_plural = 'Livros Favoritos'

    def __str__(self):
        return self.livro.titulo
