from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('top.urls')),
    path('picture/', include('picture.urls')),
    path('movie/', include('movie.urls')),
    path('modeling/', include('modeling.urls')),
    path('note/', include('note.urls')),
    #path('others/', include('others.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# +static...を追加
