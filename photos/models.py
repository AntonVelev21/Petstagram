from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import ForeignKey, CASCADE

from pets.models import Pet
from photos.validators import FileSizeValidator

User = get_user_model()
class Photo(models.Model):
    photo = models.ImageField(upload_to='images', validators=[FileSizeValidator(5)])
    description = models.CharField(max_length=300, validators=[
        MinLengthValidator(10),
    ], blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField('pets.Pet', blank=True, related_name='photos')
    date_of_publication = models.DateField(auto_now=True)
    user = ForeignKey(User, related_name='photos', on_delete=CASCADE)



