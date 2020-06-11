from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    """Post to be used for a recipe"""
    title = models.CharField(max_length=255)
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title