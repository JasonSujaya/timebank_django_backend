from rest_framework import serializers
from .models import Post, PostTag, PostTagRelation, PostImages
from post_interaction_api import models as post_interaction_models
from post_interaction_api import serializers as post_interaction_serializers
from django.core.paginator import Paginator


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ("id", "title", "description", "alt_text")


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = "__all__"


class PostTagRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTagRelation
        fields = "__all__"


class PostTagRelationObjectSerializer(serializers.ModelSerializer):
    # Serializers for Intermediary table between tag and posttag
    tag = PostTagSerializer(read_only=True)
    tag_id = serializers.PrimaryKeyRelatedField(
        write_only=True, source='tag', queryset=PostTag.objects.all())

    class Meta:
        model = PostTagRelation
        fields = ("tag", "tag_id")


class PostSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer(required=False)
    tag = PostTagRelationObjectSerializer(many=True)
    images = PostImagesSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "user_profile", "title",
                  "category", "tag", "images"]
        extra_kwargs = {'user_profile': {'read_only': True}}

    def create(self, validated_data):
        tag_data = validated_data.pop('tag')
        image_data = validated_data.pop('images')
        post = Post.objects.create(**validated_data)

        # Create Tags for Post
        for tag_item in tag_data:
            PostTagRelation.objects.create(
                post_id=post,
                tag_id=tag_item.get("tag"))
        # Create Images For Post
        for image_item in image_data:
            PostImages.objects.create(post_id=post, **image_item)

        return post

    def update(self, instance, validated_data):
        # updates the post
        instance.title = validated_data.get("title", instance.title)
        instance.category = validated_data.get(
            "category", instance.category)
        instance.save()

        # Updates Tags for Post
        tag_data = validated_data.pop('tag')
        PostTagRelation.objects.filter(post_id=instance).delete()
        for tag_item in tag_data:
            PostTagRelation.objects.create(
                post_id=instance,
                tag_id=tag_item.get("tag"))

        # Updates Images For Post
        image_data = validated_data.pop('images')
        PostImages.objects.filter(post_id=instance).delete()
        for image_item in image_data:
            PostImages.objects.create(post_id=instance, **image_item)

        return instance


class GetPostSerializer(serializers.ModelSerializer):
    tag = PostTagSerializer(many=True)
    images = serializers.SerializerMethodField('paginated_images')
    post_comments = serializers.SerializerMethodField('paginated_comments')
    post_bookmarkslist = serializers.SerializerMethodField(
        'paginated_bookmarklist')

    class Meta:
        model = Post
        fields = ["id", "title", "user_profile",
                  "category", "tag", "images", "post_comments", "post_bookmarkslist", "bookmarks"]
        extra_kwargs = {'user_profile': {'read_only': True}}

    def paginated_images(self, obj):
        paginator = Paginator(obj.images.all(), 3)
        page_number = self.context['request'].query_params.get('page') or 1
        images = paginator.page(page_number)
        serializer = PostImagesSerializer(images, many=True, read_only=True)

        return serializer.data

    def paginated_comments(self, obj):
        paginator = Paginator(obj.post_comments.all(), 3)
        page_number = self.context['request'].query_params.get('page') or 1
        post_comments = paginator.page(page_number)
        serializer = post_interaction_serializers.PostCommentSerializer(
            post_comments, many=True, read_only=True)

        return serializer.data

    def paginated_bookmarklist(self, obj):
        paginator = Paginator(obj.post_bookmarkslist.all(), 3)
        page_number = self.context['request'].query_params.get('page') or 1
        post_bookmarkslist = paginator.page(page_number)
        serializer = post_interaction_serializers.PostBookmarkSerializer(
            post_bookmarkslist, many=True, read_only=True)

        return serializer.data


# class PostTagSerializer(serializers.HyperlinkedModelSerializer):
#     # tagurl = serializers.HyperlinkedIdentityField(view_name="tag-detail")
#     id = serializers.ReadOnlyField()

#     class Meta:
#         model = PostTag
#         extra_kwargs = {
#             'url': {'view_name': 'tag-detail'}
#         }
#         fields = "__all__"
