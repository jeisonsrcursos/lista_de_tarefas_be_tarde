from uuid import uuid4

from django.db import models


"""
Função para renomear uma foto adicionada a aplicação.
Ela será utilizada no campo foto do model Tarefa.
"""
def upload_foto(instance, filename):
    return f"{uuid4}-{filename}"

"""
Model resposnsável pela persistência de dados.
Sua função é servir como um meio de comunicação entre
a aplicação e a tabela tarefa do banco de dados.
"""
class Tarefa(models.Model):
    titulo = models.CharField(max_length=60, null=False)
    descricao = models.CharField(max_length=120)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    concluida = models.BooleanField()
    foto = models.FileField(upload_to=upload_foto, blank=True, null=True)

    def __str__(self):
        return self.titulo