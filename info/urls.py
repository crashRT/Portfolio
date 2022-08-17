from django.urls import path
from .views import aboutview, contactview

urlpatterns = [
    path('about/', aboutview, name='about'),
    path('contact/', contactview, name='contact'),
]
