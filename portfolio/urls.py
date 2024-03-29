from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('', include('top.urls')),
    path('admin/', admin.site.urls),
    path('works/', include('works.urls')),
    path('projects/', include('projects.urls')),
    path('notes/', include('notes.urls')),
    path('info/', include('info.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),  # 本番環境で media ファイルを読み込ませるための設定
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
