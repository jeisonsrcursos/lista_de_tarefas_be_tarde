from rest_framework import serializers

from tarefas.models import Tarefa


"""
Serializer responsável pela troca de informação da API com
outras aplicações ou sistemas.
"""
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

