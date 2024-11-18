from django.urls import path

from tarefas.tarefas_views import TarefasAPIViews
from tarefas.views import ListarTarefaView, EditarBuscarDeletarView

urlpatterns = [
    path('v1/tarefas/', ListarTarefaView.as_view(), name='listar-criar-tarefa-view'),
    path('v1/tarefas/<int:pk>',
         EditarBuscarDeletarView.as_view(),
         name='editar-buscar-deletar-view'
    ),
    #path('v2/tarefas/',
    #     TarefasAPIViews.as_view(),
    #     name='criar-listar-editar-deletar-tarefa-view'
    #),
    #path('v2/tarefas/<int:pk>',
    #     TarefasAPIViews.as_view(),
    #     name='criar-listar-editar-deletar-tarefa-view'
    #),
]