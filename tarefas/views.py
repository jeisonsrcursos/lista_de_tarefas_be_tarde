# Versão 1 da API de tarefas

from rest_framework import generics, views, viewsets

from tarefas.models import Tarefa
from tarefas.serializers import TarefaSerializer

# API V1
# GET POST PUT PATCH DELETE

# Utiliza os Verbos HTTP => GET e POST
class ListarTarefaView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


# Utiliza os Verbos HTTP => PUT/PATCH GET DELETE
class EditarBuscarDeletarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

# API V2
class TarefaView(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
