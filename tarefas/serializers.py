from rest_framework import serializers

from tarefas.models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
        """
            * JSON => .json
            * XML => .xml
            * YAML => .yml
        """



