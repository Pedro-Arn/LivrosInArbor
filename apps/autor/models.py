# Importação da biblioteca para gerar id 
import uuid
# Importação da classe de configuração do modelo
from django.db import models
# Importação da função que transforma textos em slugs
from django.utils.text import slugify

# Definição da classe 'Autor' que herda de uma classe padrão do Django
class Autor(models.Model):
    # Todos os atributos que constaram na classe
    nome_completo = models.CharField(max_length=100) # Tipo campo de texto
    biografia = models.TextField(max_length=500, blank=True) # Tipo campo de texto longo, é opcional
    data_nascimento = models.DateField( # Tipo data
        blank=True, # É opcional 
        null=True, # Pode ser nulo
        verbose_name='Data de nascimento', # Nome que aparecerá na tela admin
    )
    slug = models.SlugField(unique=True, blank=True) # Tipo slug, é único e opcional
    foto_perfil = models.ImageField( # Tipo imagem 
        upload_to='autor', # Imagens armazenadas na pasta 'autor'
        null=True, # Pode ser nula
        blank=True, # É opcional
        default='usuario.png' # Imagem padrão para caso de não upload
    )

    # Configuração de informações adicionais
    class Meta:
        db_table  = 'autor' # Nome da tabela no BD
        # Nomes que aparecerão na tela admin
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    # Como autor será listado na tela admin
    def __str__(self):
        return self.nome_completo
    
    # Definição de comportamento ao salvar um objeto 
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nome_completo) # Cria um slug com base no nome através da função slugify
            slug = base_slug

            while Autor.objects.filter(slug=slug).exists(): # Verifica se o slug já existe no BD
                slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"  # Gera um ID único de 8-dígitos

            self.slug = slug
        
        super().save(*args, **kwargs) # Salva o objeto no BD