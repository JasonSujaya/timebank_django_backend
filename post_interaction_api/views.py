from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins

# Auth Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Authentication
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


# Import Apps & Serializers
from .serializers import PostCommentSerializer, ReportCategorySerializer, PostReportSerializer, PostCommentReportSerializer, PostBookmarkSerializer
from .models import PostComment, ReportCategory, PostReport, PostCommentReport, PostBookmark

from Timeo_Project.pagination import FivePaginationLimitOffset

# Create your views here.


class ReportCategoryViewset(viewsets.ModelViewSet):
    queryset = ReportCategory.objects.all()
    serializer_class = ReportCategorySerializer


class PostReportViewset(viewsets.ModelViewSet):
    queryset = PostReport.objects.all()
    serializer_class = PostReportSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class PostCommentReportViewset(viewsets.ModelViewSet):
    queryset = PostCommentReport.objects.all()
    serializer_class = PostCommentReportSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class PostCommentViewset(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class PostBookmarkViewset(viewsets.ModelViewSet):
    queryset = PostBookmark.objects.all()
    serializer_class = PostBookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def perform_destroy(self, instance):
        instance.post_id.bookmarks -= 1
        instance.post_id.save()
        instance.delete()


class GetPostBookmarkListAPIView(generics.ListAPIView):
    queryset = PostBookmark.objects.all()
    pagination_class = FivePaginationLimitOffset

    def get_queryset(self):
        queryset = PostBookmark.objects.filter(post_id=self.kwargs["pk"])
        return queryset
    serializer_class = PostBookmarkSerializer


class GetPostCommentListAPIView(generics.ListAPIView):
    queryset = PostComment.objects.all()
    pagination_class = FivePaginationLimitOffset

    def get_queryset(self):
        queryset = PostComment.objects.filter(post_id=self.kwargs["pk"])
        return queryset
    serializer_class = PostCommentSerializer
