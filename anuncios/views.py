from django.shortcuts import render
from django.http import HttpResponse
from anuncios import models
from .models import Categoria
from .models import Anuncio

def home(request):
    categorias = Categoria.objects.all()

    ultimos_anuncios = Anuncio.objects.all()[:12]

    return render(request, 'home.html', {'categorias': categorias, 'anuncios':ultimos_anuncios})