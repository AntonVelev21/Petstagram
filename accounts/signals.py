from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from accounts.models import Profile, AppUser

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
        send_mail(subject='User creation',
                  message=f'Congratulations {username}! You just joined Petstagram!',
                  from_email=settings.COMPANY_EMAIL,
                  recipient_list=[instance.email],
                  fail_silently=False)



@receiver(post_delete, sender=Profile)
def user_delete(sender, instance, **kwargs):
    user = instance.user
    user.delete()

