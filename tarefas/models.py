from uuid import uuid4

from django.db import models


def upload_foto(instance, filename):
    return f"{uuid4}-{filename}"

class Tarefa(models.Model):
    titulo = models.CharField(max_length=60, null=False)
    descricao = models.CharField(max_length=120)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    concluida = models.BooleanField()
    foto = models.FileField(upload_to=upload_foto, blank=True, null=True)

    def __str__(self):
        return self.titulo