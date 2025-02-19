from django.core.exceptions import ValidationError
# Importação da classe de configuração do modelo
from django.db import models
from django.contrib.auth.models import User
# Importação de classes associadas
from apps.usuario.choices import (
    Generos,
    Ocupacoes,
    Identificacoes,
)

# Validação do campo de identificação (numérico, 11 a 13 digitos)
def validar_identificacao(valor, tipo):
    if not valor.isdigit():  # Garante que seja um valor numerico
        raise ValidationError("Identificação deve ser um valor numérico.")
    
    comprimento = len(valor)

    if tipo == 'C' and comprimento != 11: # Validação CPF
        raise ValidationError("CPF deve ter 11 dígitos.")
    elif tipo == 'M' and comprimento != 13: # Validação matrícula
        raise ValidationError("Matrícula deve ter 13 dígitos.")

# Definição da classe 'Usuario' que herda de uma classe padrão do Django
class Usuario(User):
    ocupacao = models.CharField( # Tipo campo livre
        verbose_name='Ocupação',
        max_length=1,
        choices=Ocupacoes.choices, # Restringe a seleção
        null=False, # Não pode ser nulo
        blank=False, # Não é opcional
    )
    data_nascimento = models.DateField(
        null=True, # Pode ser nulo
        blank=True, # É opcional
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
        verbose_name="gênero",
        max_length=1,
        choices=Generos.choices,
        blank=False,
        null=False,
    )
    foto_perfil = models.ImageField(
        upload_to='usuario',
        null=True,
        default='usuario.png',
    )

    @property
    def nome_completo(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    # Validação personalizada para o campo identificação
    def clean(self):
        super().clean()
        validar_identificacao(self.identificacao, self.tipo_identificacao)

    # Configuração de informações adicionais
    class Meta:
        db_table  = 'usuario'

class Favoritos(models.Model):
    from apps.livros.models import Livros
    # Todos os atributos que constaram na classe (composição)
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

    # Como livro será listado na tela admin
    def __str__(self):
        return self.livro.titulo
