from django.urls import path
from rest_framework import routers
from tarefas.views import (
    ListarTarefaView,
    EditarBuscarDeletarView,
    TarefaView
)

# API V1
urlpatterns = [
    path('tarefas/',
         ListarTarefaView.as_view(),
         name='listar-criar-tarefa-view'),
    path('tarefas/<int:pk>',
         EditarBuscarDeletarView.as_view(),
         name='editar-buscar-deletar-view'
    ),
]

# API V2
router = routers.SimpleRouter()
router.register(
    r'tarefas',
    TarefaView,
    basename='crud-tarefa-view'
)