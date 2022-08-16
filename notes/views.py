from django.shortcuts import render
from .models import NotesModel, tags

# Create your views here.


def noteslistview(request):
    notes_list = NotesModel.objects.order_by("date")
    context = {
        'notes_list': notes_list,
        'taglist': tags
    }
    return render(request, 'notes/list.html', context)


def notestagview(requested, tagname):
    notes_list = NotesModel.objects.filter(tag__in=[tagname]).distinct()
    context = {
        'notes_list': notes_list,
        'taglist': tags,
    }
    return render(requested, 'notes/list.html', context)
