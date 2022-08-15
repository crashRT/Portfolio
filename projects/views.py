from django.shortcuts import render
from .models import ProjectsModel, tags

# Create your views here.

def projectslistview(request):
    projects_list = ProjectsModel.objects.all()
    context = {
        'projects_list':projects_list,
        'taglist':tags
    }
    return render(request, 'projects/list.html', context)

def projectdetailview(request, pk):
    project_list = ProjectsModel.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project_list': project_list})

def workstagview(requested, tagname):
    projects_list = ProjectsModel.objects.filter(tag__in=[tagname]).distinct()
    context = {
        'projects_list': projects_list,
        'taglist': tags,
    }
    return render(requested, 'works/list.html', context)