from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PictureModel

class PictureList(ListView):
    template_name = 'PictureList.html'
    model = PictureModel

class PictureDetail(DetailView):
    template_name = 'PictureDetail.html'
    model = PictureModel