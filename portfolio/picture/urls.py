from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import PictureList

urlpatterns = [
    path('list/', PictureList.as_view()),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
