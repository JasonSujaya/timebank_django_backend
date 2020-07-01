from django.contrib import admin
from .models import Post, PostCategory, PostImages, Tag, PostTagRelation
# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(PostImages)
admin.site.register(Tag)
admin.site.register(PostTagRelation)
