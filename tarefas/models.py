from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=60, null=False)
    descricao = models.CharField(max_length=120)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    concluida = models.BooleanField()

    def __str__(self):
        return self.titulo