from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import ReportCategoryViewset, PostCommentViewset, PostCommentReportViewset, PostReportViewset

router = DefaultRouter()
router.register('report-category', ReportCategoryViewset,
                base_name='report-category')
router.register('post-comment', PostCommentViewset,
                base_name='post-comment')
router.register('post-report_comment', PostCommentReportViewset,
                base_name='post-report_comment')
router.register('post-report', PostReportViewset,
                base_name='post-report')

urlpatterns = [
    path('', include(router.urls)),
]
