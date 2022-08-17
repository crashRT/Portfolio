from django.shortcuts import render
from .models import WorksModel, tags


# Create your views here.


def worklistview(request):
    work_list = WorksModel.objects.order_by('date').reverse()
    context = {
        'works_list': work_list,
        'taglist': tags,
    }
    return render(request, 'works/list.html', context)


def workdetailview(request, pk):
    work = WorksModel.objects.get(pk=pk)
    return render(request, 'works/detail.html', {'work': work})


def workstagview(requested, tagname):
    work_list = WorksModel.objects.filter(
        tag__in=[tagname]).distinct().order_by('date').reverse()
    context = {
        'works_list': work_list,
        'taglist': tags,
    }
    return render(requested, 'works/list.html', context)
