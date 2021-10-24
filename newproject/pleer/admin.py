from django.contrib import admin

# Register your models here.
from .models import Composition, PlayList

admin.site.register(Composition)
admin.site.register(PlayList)