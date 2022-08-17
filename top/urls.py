
from django.urls import path
from .views import topview
urlpatterns = [
    path('', topview, name='top'),
]
