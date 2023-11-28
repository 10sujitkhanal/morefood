from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

@receiver(post_save, sender=get_user_model())
def assign_permissions(sender, instance, created, **kwargs):
    per = Permission.objects.all()
    if created and instance.is_restaurant_user:
        permissions_list = [
            'view_order', 
            'add_fooditem',
            'change_fooditem',
            'delete_fooditem',
            'view_fooditem',
            'add_menu',
            'change_menu',
            'delete_menu',
            'view_menu',
        ]
        permissions = Permission.objects.filter(codename__in=permissions_list)
        instance.user_permissions.add(*permissions)
        instance.is_staff = True
