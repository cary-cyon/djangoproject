from django.shortcuts import render
from django.http import HttpResponse
from .models import Composition
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    all_composition = Composition.objects.all()
    pages = Paginator(all_composition, 1)
    page = pages.get_page(request.GET.get('page'))
    return render(request, 'pleer/list.html', {'all_composition': page})


def test(request):
    return HttpResponse("SDFGHJKL:JHGFDSASD")
