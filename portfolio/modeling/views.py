from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import ModelingModel

class ModelingList(ListView):
    template_name = 'ModelingList.html'
    model = ModelingModel

class ModelingDetail(DetailView):
    template_name = 'ModelingDetail.html'
    model = ModelingModel