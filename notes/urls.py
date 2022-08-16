
from django.urls import path
from .views import noteslistview, notestagview

urlpatterns = [
    path('', noteslistview, name='noteslist'),
    path('category/<str:tagname>', notestagview, name='notestag'),
]
