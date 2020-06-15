from rest_framework import serializers
from .models import PostComment, PostCommentReport, PostReport, PostBookmark, ReportCategory


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
