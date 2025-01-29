from django.db import models

class Materias(models.Model):

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

    nome = models.CharField(max_length=70, blank=False, null=False)
    fase_basica = models.BooleanField()
    periodo = models.IntegerField(
        choices=PERIODOS_CHOICES,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.nome + ' - ' + str(self.periodo)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['periodo',]


class Cursos(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    materias = models.ManyToManyField(Materias)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome',]
