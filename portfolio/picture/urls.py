from django.urls import path
from .views import PictureList

urlpatterns = [
    path('list/', PictureList.as_view()),
]