from django.contrib import admin
from .models import PostComment, PostBookmark, ReportCategory, PostReport, PostCommentReport

# Register your models here.
admin.site.register(PostComment)
admin.site.register(PostBookmark)
admin.site.register(ReportCategory)
admin.site.register(PostReport)
admin.site.register(PostCommentReport)
