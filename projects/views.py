from django.shortcuts import render
from .models import ProjectsModel

# Create your views here.

def projectslistview(request, pk):
    projects = ProjectsModel.objects.all()
    return render(request, 'projects/detail.html', {'projects':projects})

def projectdetailview(request, pk):
    project = ProjectsModel.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})