from django.contrib.auth import models as auth_models, get_user_model
from django.db import models
from django.db.models import TextChoices

from accounts.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



UserModel = get_user_model()


class Profile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GenderChoices.choices)



