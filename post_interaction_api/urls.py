from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import ReportCategoryViewset, PostCommentViewset, PostCommentReportViewset, PostReportViewset, PostBookmarkViewset

router = DefaultRouter()
router.register('report-category', ReportCategoryViewset,
                base_name='report-category')
router.register('comment', PostCommentViewset,
                base_name='comment')
router.register('report-comment', PostCommentReportViewset,
                base_name='report_comment')
router.register('report-post', PostReportViewset,
                base_name='report-post')
router.register('bookmark', PostBookmarkViewset,
                base_name='bookmark')

urlpatterns = [
    path('', include(router.urls)),
]
