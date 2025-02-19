# Importação da classe de configuração do modelo
from django.db import models
# Importação da função que transforma textos em slugs
from django.utils.text import slugify

# Importação das classes de associação
from apps.autor.models import Autor
from apps.curso.models import Materias

# Definição da classe 'Editora' que herda de uma classe padrão do Django
class Editora(models.Model):
    nome = models.CharField( # Tipo campo de texto
        max_length=100,
        null=False, # Não pode ser nulo
        unique=True, # É único
    )

    # Como editora será listada na tela admin
    def __str__(self):
        return self.nome

    # Configuração de informações adicionais
    class Meta:
        db_table = 'editora'


class Link(models.Model):
    site = models.CharField(
        'Site de compra', 
        max_length=100,
        blank=False,
        null=False,
    )
    link = models.TextField(
        'Link do site',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.site

    class Meta:
        db_table = 'Link'


class Livros(models.Model):
    titulo = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=False,
    )
    descricao = models.TextField(max_length=500, blank=True)
    ano_publicacao = models.DateField(
        verbose_name='Data de publicação',
        blank=True,
        null=True
    )
    editora = models.ForeignKey(
        Editora,
        on_delete=models.CASCADE, # Será deletada se o livro também for
        blank=False,
        null=True
    )
    links = models.ManyToManyField(
        Link,
        blank=True,
        verbose_name='Onde comprar',
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
        related_name='livros',
    )
    materia = models.ManyToManyField(
        Materias,
        related_name='materia_livro',
        verbose_name='Materias associadas',
    )
    slug = models.SlugField(unique=True, blank=True)
    capa = models.ImageField(
        upload_to='livros', 
        null=True, 
        blank=True,
        default='capa_base.png'
    )

    class Meta:
        db_table = 'livros'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo',]

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class Comentario(models.Model):
    # Importação da classe de associação
    from apps.usuario.models import Usuario

    livro = models.ForeignKey(
        Livros,
        on_delete=models.CASCADE, # Será deletado se o livro também for
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE, # Será deletado se o usuario também for
    )
    corpo = models.TextField()
    postado_em = models.DateTimeField(auto_now_add=True) # Tipo data e hora, salva infos atuais

    class Meta:
        ordering = ['postado_em',]

    def __str__(self):
        return f'{self.livro.titulo} por {self.usuario.first_name}'
