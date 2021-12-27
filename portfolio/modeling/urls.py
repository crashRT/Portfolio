from django.urls import path
from .views import ModelingList, ModelingDetail

urlpatterns = [
    path('', ModelingList.as_view(), name = 'ModelingList'),
    path('detail/<int:pk>/',ModelingDetail.as_view(), name = 'ModelingDetail'),
]