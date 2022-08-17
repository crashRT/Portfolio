from django.urls import path
from .views import worklistview, workdetailview, workstagview

urlpatterns = [
    path('', worklistview, name='worklist'),
    path('detail/<int:pk>/', workdetailview, name='workdetail'),
    path('category/<str:tagname>', workstagview, name='worktag'),
]
