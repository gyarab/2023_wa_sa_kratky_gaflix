from django.shortcuts import render

from filmy.models import Movie

def index(request):
    
    return render(request, 'filmy/base.html')

def movies(register):

    context = {
        'movies': Movie.objects.all().order_by('name')
    }

    return render(register, 'filmy/movies.html', context)

def movie(request, id):
    
    context = {
        'movie': Movie.objects.get(id=id)
    }

    return render(register, 'filmy/movie.html', context)