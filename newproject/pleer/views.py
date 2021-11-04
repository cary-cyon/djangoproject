from django.shortcuts import render
from django.http import HttpResponse
from .models import Composition
# Create your views here.


def index(request):
    all_composition = Composition.objects.all()
    return render(request, 'pleer/list.html', {'all_composition': all_composition})


def test(request):
    return HttpResponse("SDFGHJKL:JHGFDSASD")
