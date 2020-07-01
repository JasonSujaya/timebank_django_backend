from django.db import models
from django.conf import settings
from profiles_api import models as profiles_models
from django.core.paginator import Paginator

import datetime


# Create your models here.


class PostCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class PostTag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    """Post to be used for a recipe"""
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PostCategory, on_delete=models.CASCADE)
    bookmarks = models.IntegerField(default=0)
    tag = models.ManyToManyField(PostTag, through='PostTagRelation')
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['category']),
        ]


class PostTagRelation(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(PostTag, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['post_id', 'tag_id']]

    def __str__(self):
        return self.post_id.title


class PostImages(models.Model):
    post_id = models.ForeignKey(
        Post, related_name="images", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title
