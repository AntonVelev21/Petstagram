from django.db import models
from django.db.models import CASCADE

from photos.models import Photo


class Comment(models.Model):
    text = models.TextField()
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey('photos.Photo', on_delete=CASCADE, related_name='comments')

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey('photos.Photo', on_delete=CASCADE, related_name='likes')

