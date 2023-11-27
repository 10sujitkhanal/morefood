from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

@receiver(post_save, sender=get_user_model())
def assign_permissions(sender, instance, created, **kwargs):
    per = Permission.objects.all()
    for p in per:
        print(p.codename)
    if created and instance.is_restaurant_user:
        # permission_name = 'Can view menu'
        # permission = Permission.objects.get(codename=permission_name)
        # instance.user_permissions.add(permission)
        pass
