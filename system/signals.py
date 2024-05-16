from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def setup_permissions_and_roles(sender, **kwargs):
    from system.models import CustomPermission

    if not CustomPermission.objects.exists():
        call_command("setup")
