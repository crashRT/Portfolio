from django.shortcuts import render
from .models import ProjectsModel

# Create your views here.

def projectsdetailview(request, pk):
    work = ProjectsModel.objects.get(pk=pk)
    return render(request, 'works/workdetail.html', {'work': work})

def projectdetailview(request, pk):
    work = ProjectsModel.objects.get(pk=pk)
    return render(request, 'works/workdetail.html', {'work': work})