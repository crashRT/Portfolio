from django.urls import path
from .views import NoteList, NoteDetail

urlpatterns = [
    path('', NoteList.as_view(), name = 'NoteList'),
    path('detail/<int:pk>/',NoteDetail.as_view(), name = 'NoteDetail'),
]