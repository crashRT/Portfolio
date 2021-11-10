from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NoteModel
# Create your views here.


class NoteList(ListView):
    template_name = 'NoteList.html'
    model = NoteModel

class NoteDetail(DetailView):
    template_name = 'NoteDetail.html'
    model = NoteModel