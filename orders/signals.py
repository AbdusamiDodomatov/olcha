from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from products.models import Product
from .models import Favorite


@receiver(post_delete, sender=Product)
def delete_favorites_when_product_deleted(sender, instance, **kwargs):
    count, _ = Favorite.objects.filter(product=instance).delete()
    print(f"[SIGNAL] Удалено {count} избранных записей для удалённого продукта: {instance}")


@receiver(post_delete, sender=settings.AUTH_USER_MODEL)
def delete_favorites_when_user_deleted(sender, instance, **kwargs):
    """Удаляем избранные товары, если пользователь удалён"""
    count, _ = Favorite.objects.filter(user=instance).delete()
    print(f"[SIGNAL] Удалено {count} избранных записей для удалённого пользователя: {instance}")
