from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DetailedInfo


@receiver(post_save, sender=DetailedInfo)
def create_detailed_info_url(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        post_url = post.get_detailed_info_url()
        if post_url:
            post.save()
