from django.db import models
from django.contrib.auth.models import AbstractUser


def user_icon_upload_path(instance, filename):
    return f"user_icon/{instance.username}/{filename}"


class CustomUser(AbstractUser):
    user_icon = models.ImageField(upload_to=user_icon_upload_path, default="user_icon/default.png")
    username = models.CharField(max_length=50, unique=True)
    verified_email = models.BooleanField(default=False)
    confirm_email_cod = models.CharField(max_length=7, blank=True, null=True)

    USERNAME_FIELD = "username"
