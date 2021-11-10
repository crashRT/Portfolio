from django.shortcuts import render
from django.views.generic import ListView
from picture.models import PictureModel
from movie.models import MovieModel

class Top(ListView):
    template_name = 'Top.html'
    model = MovieModel

    def get_context_data(self):
        context = super(Top, self).get_context_data()
        context.update({
            'object_list2': PictureModel.objects.all(),
        })
        return context