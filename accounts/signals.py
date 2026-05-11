from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile

User = get_user_model()

'''
Profile creation when user is registered with default username
'''
@receiver(post_save, sender=User)
def profile_create(sender, instance, created, **kwargs):
    index = instance.email.index('@')
    username = instance.email[0:index]
    if created:
        profile = Profile.objects.create(
            username=username,
            user=instance
        )
        profile.save()