from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import profile, Location

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=profile)
def create_profile_Location(sender, instance, created, **kwargs):
    if created:
        profile_Location = Location.objects.create()
        instance.location = profile_Location
        instance.save()

@receiver(post_delete, sender = profile)
def delete_profile_Location(sender, instance, *args, **kwargs):
    if instance.location :
        instance.location.delete()