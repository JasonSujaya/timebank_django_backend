from django.db import models
from django.conf import settings
from profiles_api import models as profiles_models
from post_api import models as post_api_models
from django.core.paginator import Paginator
from django.utils import timezone

import datetime

# Create your models here.


class PostComment(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, related_name="postuser_comments", on_delete=models.CASCADE)
    post_id = models.ForeignKey(
        post_api_models.Post, related_name="post_comments", on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    pending = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.message


class PostBookmark(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, related_name="user_bookmarkslist", on_delete=models.CASCADE)
    post_id = models.ForeignKey(
        post_api_models.Post, related_name="post_bookmarkslist", on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.post_id.title

    # class Meta:
        # unique_together = [['post_id', 'user_id']]


class ReportCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class PostReport(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(post_api_models.Post, on_delete=models.CASCADE)
    category = models.OneToOneField(ReportCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.post_id.title


class PostCommentReport(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    category = models.OneToOneField(ReportCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.comment_id.message
