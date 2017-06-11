from django.db import models


# Create your models here.
#  model for album and song

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=50)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' By ' + self.artist


class Song(models.Model):
    album = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    models.ForeignKey(Album)

