from django.db import models
from django.conf import settings
from profiles_api import models as profiles_models
from django.core.paginator import Paginator
from django.utils import timezone

from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import BrinIndex
from django.contrib.postgres.indexes import GinIndex
import datetime


# Create your models here.
class PostCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    """Post to be used for a recipe"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        PostCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    title_content_search = SearchVectorField(null=True)
    bookmarks = models.IntegerField(default=0)
    visible = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        default=timezone.now)

    tag = models.ManyToManyField(Tag, through='PostTag')

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            BrinIndex(fields=['created_date']),
            models.Index(fields=['id', 'category']),
            GinIndex(fields=["title_content_search"])
        ]


class PostTag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['post_id', 'tag_id']]

    def __str__(self):
        return self.post_id.title


class PostImages(models.Model):
    post_id = models.ForeignKey(
        Post, related_name="images", on_delete=models.CASCADE)
    image_path = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
