from rest_framework import serializers
from .models import PostComment, PostCommentReport, PostReport, PostBookmark, ReportCategory
from post_api import models as post_api_models


class ReportCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCategory
        fields = "__all__"


class PostReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReport
        fields = "__all__"
        extra_kwargs = {'user_id': {'read_only': True}}


class PostCommentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCommentReport
        fields = "__all__"
        extra_kwargs = {'user_id': {'read_only': True}}


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ("__all__")
        extra_kwargs = {'user_id': {'read_only': True}}


class PostBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostBookmark
        fields = "__all__"
        extra_kwargs = {'user_id': {'read_only': True}}

    def create(self, validated_data):
        # Edit the bookmark value in post_bookmark
        post_id = validated_data.get('post_id')
        post_id.bookmarks += 1
        post_id.save()
        # Create the bookmark value
        bookmark = PostBookmark.objects.create(**validated_data)
        return bookmark

