from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Serie, Livre


class SerieListView(generic.ListView):
    model = Serie
    #paginate_by = 100
    ordering = 'nom'
    def get_context_data(self, **kwargs): #Ne rien mettre dois faire la même chose!
        context = super().get_context_data(**kwargs)
        return context


class SerieDetailView(generic.DetailView):
    model = Serie
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livres'] = context['object'].livre_set.all().order_by('tome')
        return context

class LivreDetailView(generic.DetailView):
    model = Livre
