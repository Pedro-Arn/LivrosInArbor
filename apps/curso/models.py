# Importação da classe de configuração do modelo
from django.db import models

# Definição da classe 'Materias' que herda de uma classe padrão do Django
class Materias(models.Model):
    
    # Período com o parâmetro choices que aceita apenas uma seleção
    PERIODOS_CHOICES = [
        (1, '1° período'),
        (2, '2° período'),
        (3, '3° período'),
        (4, '4° período'),
        (5, '5° período'),
        (6, '6° período'),
        (7, '7° período'),
        (8, '8° período'),
        (9, '9° período'),
        (10, '10° período'),
    ]

    nome = models.CharField(max_length=70, blank=False, null=False) # Tipo campo de texto
    fase_basica = models.BooleanField() # Tipo booleano
    periodo = models.IntegerField( # Tipo inteiro
        choices=PERIODOS_CHOICES,
        null=False, # Não pode ser nulo
        blank=False, # Não é opcional
    )
    
    # Como período será listado na tela admin
    def __str__(self):
        return self.nome + ' - ' + str(self.periodo)
 
    # Configuração de informações adicionais
    class Meta:
        db_table  = 'materias'  # Nome da tabela no BD
        # Nomes que aparecerão na tela admin
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['periodo',]


class Cursos(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    materias = models.ManyToManyField(Materias)

    def __str__(self):
        return self.nome

    class Meta:
        db_table  = 'cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome',]
