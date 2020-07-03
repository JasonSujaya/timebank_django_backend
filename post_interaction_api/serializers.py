from rest_framework import serializers
from .models import PostComment, PostCommentReport, PostReport, PostBookmark, ReportCategory
from post_api import models as post_api_models
from django.utils import timezone


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
        fields = ("id", "message", "user_id", "post_id")
        extra_kwargs = {'user_id': {'read_only': True}}

    # prevent creation of more than 5 comments per post under 5 minute
    def create(self, validated_data):
        user = self.context['request'].user
        time_limit = timezone.now() - timezone.timedelta(minutes=5)
        comment_list = PostComment.objects.filter(user_id=user, post_id=validated_data["post_id"].id, created_date__range=[
            time_limit, timezone.now(), ])
        if (comment_list.count() <= 5):
            comments = PostComment.objects.create(**validated_data)
            return comments
        else:
            print("Too much tags COMMENTS ON POST")
            pass


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
