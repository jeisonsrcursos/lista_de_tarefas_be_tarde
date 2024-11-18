
from django.contrib import admin
from django.urls import path, include

from tarefas.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tarefas.urls')),
    path('api/v2/', include(router.urls))
]
