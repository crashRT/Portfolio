from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import PictureList, PictureDetail

urlpatterns = [
    path('list/', PictureList.as_view()),
    path('detail/<int:pk>/',PictureDetail.as_view()),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
