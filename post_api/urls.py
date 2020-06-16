from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import PostTagViewset, PostManagerView, PostTagRelationViewset, PostImages, GetImageListAPIView
from post_interaction_api import views as post_interaction_views

router = DefaultRouter()
router.register('tag', PostTagViewset,
                base_name='tag')
router.register('post-manager', PostManagerView,
                base_name='post-manager')
router.register('post-tag', PostTagRelationViewset,
                base_name='post-tag')
router.register('post-images', PostTagRelationViewset,
                base_name='post-images')


urlpatterns = [
    path('', include(router.urls)),
    path('post-manager/<int:pk>/images/', GetImageListAPIView.as_view()),
    path('post-manager/<int:pk>/bookmarks/',
         post_interaction_views.GetPostBookmarkListAPIView.as_view()),
    path('post-manager/<int:pk>/comments/',
         post_interaction_views.GetPostCommentListAPIView.as_view()),
]
