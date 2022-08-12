from django.urls import path
from .views import worklistview, workdetailview

urlpatterns = [
    path('', worklistview, name='worklist'),
    path('<int:pk>/', workdetailview, name='workdetail')
]
