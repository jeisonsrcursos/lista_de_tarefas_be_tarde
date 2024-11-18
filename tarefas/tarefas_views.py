# Versão 2 da API de tarefas
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

from tarefas.models import Tarefa
from tarefas.serializers import TarefaSerializer

# Utiliza os verbos HTTP => GET POST PUT PATCH DELETE
class TarefasAPIViews(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

