from rest_framework import serializers
from .models import Post, Tag, PostTag, PostImages
from post_interaction_api import models as post_interaction_models
from post_interaction_api import serializers as post_interaction_serializers
from django.core.paginator import Paginator
from django.utils import timezone


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ("id", "title", "description", "alt_text")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["tag_name", "id", "user"]
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user
        time_limit = timezone.now() - timezone.timedelta(hours=8)
        tag_list = Tag.objects.filter(user=user, created_date__range=[
            time_limit, timezone.now(), ])

        # prevent creation of more than 5 tags under 8 hour
        if (tag_list.count() <= 5):
            lower_case_name = validated_data['tag_name'].lower()
            tag = Tag.objects.create(
                tag_name=lower_case_name, user=user)
            return tag
        else:
            print("Too much tags ERROR")
            pass


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = "__all__"


class PostTagObjectSerializer(serializers.ModelSerializer):
    # Serializers for Intermediary table between tag and posttag
    tag = TagSerializer(read_only=True)
    tag_id = serializers.PrimaryKeyRelatedField(
        write_only=True, source='tag', queryset=Tag.objects.all())

    class Meta:
        model = PostTag
        fields = ("tag", "tag_id")


class PostSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer(required=False)
    tag = PostTagObjectSerializer(many=True)
    images = PostImagesSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "user", "title", "content",
                  "category", "tag", "images"]
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user
        time_limit = timezone.now() - timezone.timedelta(hours=8)
        post_list = Post.objects.filter(user=user, created_date__range=[
            time_limit, timezone.now(), ])

        # prevent creation of more than 5 post under 8 hour
        if (post_list.count() <= 5):
            tag_data = validated_data.pop('tag')
            image_data = validated_data.pop('images')
            post = Post.objects.create(**validated_data)
            post.save()
            post = Post.objects.get(id=post.id)
            post.full_title_content = post.title + " " + post.content
            post.save()

            # Create Tags for Post
            for tag_item in tag_data:
                PostTag.objects.create(
                    post_id=post,
                    tag_id=tag_item.get("tag"))
            # Create Images For Post
            for image_item in image_data:
                PostImages.objects.create(post_id=post, **image_item)

            return post
        else:
            print("Too much tags ERROR")
            pass

    def update(self, instance, validated_data):
        # updates the post
        instance.title = validated_data.get("title", instance.title)
        instance.category = validated_data.get(
            "category", instance.category)
        instance.content = validated_data.get(
            "content", instance.content)
        instance.full_title_content = str(validated_data.get("title", instance.title) + " " + validated_data.get(
            "content", instance.content))

        instance.save()

        # Updates Tags for Post
        tag_data = validated_data.pop('tag')
        PostTag.objects.filter(post_id=instance).delete()
        for tag_item in tag_data:
            PostTag.objects.create(
                post_id=instance,
                tag_id=tag_item.get("tag"))

        # Updates Images For Post
        image_data = validated_data.pop('images')
        PostImages.objects.filter(post_id=instance).delete()
        for image_item in image_data:
            PostImages.objects.create(post_id=instance, **image_item)

        return instance


class GetPostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    images = serializers.SerializerMethodField('paginated_images')
    post_comments = serializers.SerializerMethodField('paginated_comments')
    post_bookmarkslist = serializers.SerializerMethodField(
        'paginated_bookmarklist')

    class Meta:
        model = Post
        fields = ["id", "title", "user", "content",
                  "category", "tag", "images", "post_comments", "post_bookmarkslist", "bookmarks"]
        extra_kwargs = {'user': {'read_only': True}}

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


# class TagSerializer(serializers.HyperlinkedModelSerializer):
#     # tagurl = serializers.HyperlinkedIdentityField(view_name="tag-detail")
#     id = serializers.ReadOnlyField()

#     class Meta:
#         model = PostTag
#         extra_kwargs = {
#             'url': {'view_name': 'tag-detail'}
#         }
#         fields = "__all__"
