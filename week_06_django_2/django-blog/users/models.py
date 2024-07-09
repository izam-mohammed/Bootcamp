from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Ünvan"
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name="Açıklama",
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="users/",
        default="def_user.png",
        verbose_name="Görsel",
    )

    # We will define the signals so that our profile model is created automatically when the User instance is created.
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserDetail.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userdetail.save()

    def __str__(self):
        return self.user.username
