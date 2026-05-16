from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE, ForeignKey

from photos.models import Photo


User = get_user_model()

class Comment(models.Model):
    text = models.TextField()
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey('photos.Photo', on_delete=CASCADE, related_name='comments')
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey('photos.Photo', on_delete=CASCADE, related_name='likes')
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

