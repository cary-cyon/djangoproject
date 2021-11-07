from django.shortcuts import render
from django.http import HttpResponse
from .models import Music, Album
# Create your views here.
def index(request):
    music=Music.objects.all()
    return render(request, 'playlists.html', {
        'music':music
    })
