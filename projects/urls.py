
from django.urls import path
from .views import projectslistview, projectdetailview

urlpatterns = [
    path('', projectslistview, name='projectslist'),
    path('detail/<int:pk>/', projectdetailview, name='projectdetail'),
]