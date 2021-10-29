from django.db import models

# Create your models here.

"""класс плейлиста """


class PlayList(models.Model):
    name = models.CharField("Playlist name", max_length=200)
    cover = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.name


""" класс композиции """


class Composition(models.Model):
    name = models.CharField("composition name", max_length=200)
    author = models.CharField("author name", max_length=200)
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to="images", null=True)
    audio = models.FileField(upload_to="audios", null=True)

    def __str__(self):
        return self.name

