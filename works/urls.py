from django.urls import path
from .views import worklistview

urlpatterns = [
    path('', worklistview, name='worklist'),
]
