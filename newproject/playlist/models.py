from django.db import models

# Create your models here.
class Music(models.Model):
    title=models.CharField(max_length=250)
    artist=models.CharField(max_length=250)
    album=models.ForeignKey('Album',null=True,blank=True,on_delete=models.SET_NULL)
    music_duration=models.DecimalField(blank=True,max_digits=20,decimal_places=2)
    audio_file=models.FileField(upload_to="audios/")
    cover_image=models.ImageField(upload_to="images/")

    def save(self,*args,**kwargs):
        if not self.music_duration:
            #logic for getting music length
            pass
            return super().save(*args, **kwargs)

class Album(models.Model):
    name=models.CharField(max_length=250)