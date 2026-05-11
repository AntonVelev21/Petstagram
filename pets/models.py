from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.utils.text import slugify

User = get_user_model()

class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    user = ForeignKey(User, related_name='pets', on_delete=CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.id}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
