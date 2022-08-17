from django.shortcuts import render
from .models import ProjectsModel, tags

# Create your views here.


def projectslistview(request):
    projects_list = ProjectsModel.objects.order_by('date').reverse()
    context = {
        'projects_list': projects_list,
        'taglist': tags
    }
    return render(request, 'projects/list.html', context)


def projectsdetailview(request, pk):
    project = ProjectsModel.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})


def projectstagview(requested, tagname):
    projects_list = ProjectsModel.objects.filter(
        tag__in=[tagname]).distinct().order_by('date').reverse()
    context = {
        'projects_list': projects_list,
        'taglist': tags,
    }
    return render(requested, 'projects/list.html', context)
