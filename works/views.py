from django.shortcuts import render
from .models import WorksModel, tags


# Create your views here.


def worklistview(request):
    work_list = WorksModel.objects.all()
    context = {
        'works_list': work_list,
        'taglist': tags,
    }
    return render(request, 'works/workslist.html', context)


def workdetailview(request, pk):
    work = WorksModel.objects.get(pk=pk)
    return render(request, 'works/workdetail.html', {'work': work})


def workstagview(requested, tagname):
    work_list = WorksModel.objects.filter(tag__in=[tagname]).distinct()
    context = {
        'works_list': work_list,
        'taglist': tags,
    }
    return render(requested, 'works/workslist.html', context)
