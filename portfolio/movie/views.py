from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MovieModel

class MovieList(ListView):
    template_name = 'MovieList.html'
    model = MovieModel

class MovieDetail(DetailView):
    template_name = 'MovieDetail.html'
    model = MovieModel