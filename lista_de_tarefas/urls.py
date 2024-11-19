from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from tarefas.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tarefas.urls')),
    path('api/v2/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
