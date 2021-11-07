from django.shortcuts import render
from pleer.models import Composition


def index(request):
    compositions = Composition.objects.all()
    return render(request, 'playlist/playlist.html', {'title': 'Список треков', 'compositions': compositions})
