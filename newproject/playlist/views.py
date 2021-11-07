from django.shortcuts import render
from pleer.models import Composition, PlayList


def index(request):
    compositions = Composition.objects.all()
    return render(request, 'playlist/playlist.html', {'title': 'Список треков', 'compositions': compositions})


def getPlaylists(request):
    playlists = PlayList.objects.all()
    compositions = Composition.objects.filter(PlayList.name == Composition.name)
    return render(request, 'playlist/all_playlists.html', {'title': 'Список плейлистов', 'playlists': playlists, 'compositions': compositions})
