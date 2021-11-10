from django.shortcuts import render
from django.views.generic import ListView
from note.models import NoteModel

# Create your views here.
class About(ListView):
    template_name = 'About.html'
    model = NoteModel

class Contact(ListView):
    template_name = 'Contact.html'
    model = NoteModel