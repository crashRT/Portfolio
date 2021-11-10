from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.
class About(DetailView):
    template_name = 'About.html'

class Contact(DetailView):
    template_name = 'Contact.html'