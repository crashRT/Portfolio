from django.shortcuts import render
from .models import WorksModel


# Create your views here.


def worklistview(request):
    work_list = WorksModel.objects.all()
    return render(request, 'works/workslist.html', {'works_list': work_list})


def workdetailview(request, pk):
    work = WorksModel.objects.get(pk=pk)
    return render(request, 'works/workdetail.html', {'work': work})
