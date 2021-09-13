from django.shortcuts import render
from django.views.generic import ListView
from .models import PictureModel

class PictureList(ListView):
    template_name = 'list.html'
    model = PictureModel
