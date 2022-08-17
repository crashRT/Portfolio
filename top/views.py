from django.shortcuts import render
from works.models import WorksModel
from projects.models import ProjectsModel
from notes.models import NotesModel

# Create your views here.


def topview(request):
    works_list = WorksModel.objects.all()[:6]
    projects_list = ProjectsModel.objects.all()[:3]
    notes_list = NotesModel.objects.all()[:4]
    context = {
        'works_list': works_list,
        'projects_list': projects_list,
        'notes_list': notes_list,
    }
    return render(request, 'top/index.html', context)