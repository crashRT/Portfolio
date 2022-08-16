from django.urls import path
from .views import projectslistview, projectsdetailview, projectstagview

urlpatterns = [
    path('', projectslistview, name='projectslist'),
    path('detail/<int:pk>/', projectsdetailview, name='projectsdetail'),
    path('category/<str:tagname>', projectstagview, name='projectstag'),
]
