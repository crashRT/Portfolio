from django.urls import path
from .views import PictureList, PictureDetail

urlpatterns = [
    path('', PictureList.as_view(), name = 'PictureList'),
    path('detail/<int:pk>/',PictureDetail.as_view(), name = 'PictureDetail'),
]
