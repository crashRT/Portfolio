from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('top.urls')),
    path('admin/', admin.site.urls),
    path('works/', include('works.urls')),
    path('projects/', include('projects.urls')),
    path('notes/', include('notes.urls')),
    path('info/', include('info.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
