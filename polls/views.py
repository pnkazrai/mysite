from django.http import HttpResponse
from django.template import loader
from .models import Album, Song


def index(request):
    album = Album.objects.all()
    song = Song.objects.all()
    templet = loader.get_template('polls/id.html')
    context = {
         'album' : album ,
         'song' : song
    }
    return HttpResponse(templet.render(context, request))


def detail(request, album_id):
    album = Album.objects.all()
    song = Song.objects.all()
    templet = loader.get_template('polls/albumDetails.html')
    context = {
        'album': album,
        'song': song
    }
    return HttpResponse(templet.render(context, request))