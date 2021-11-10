from django.urls import path
from .views import MovieList, MovieDetail

urlpatterns = [
    path('', MovieList.as_view(), name = 'MovieList'),
    path('detail/<int:pk>/',MovieDetail.as_view(), name = 'MovieDetail'),
]
