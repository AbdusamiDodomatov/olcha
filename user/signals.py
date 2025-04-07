import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from orders.models import Favorite
from django.apps import apps

logger = logging.getLogger(__name__)

User = settings.AUTH_USER_MODEL
Profile = apps.get_model('user', 'Profile')

@receiver(post_save, sender=User)
def create_favorite_default(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL] Новый пользователь создан: {instance}")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(f'[SIGNAL] Профиль создан для пользователя: {instance}')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    print(f'[SIGNAL] Профиль обновлён для пользователя: {instance}')
