from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins, filters

# Auth Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Authentication
from rest_framework.authentication import TokenAuthentication
from post_api import permissions

# Import Apps & Serializers
from .serializers import PostSerializer, GetPostSerializer, PostTagSerializer, PostTagRelationSerializer, PostImagesSerializer
from .models import Post, PostTag, PostTagRelation, PostImages

from Timeo_Project.pagination import FivePaginationLimitOffset


class PostManagerView(viewsets.ModelViewSet):
    """Handles Authentication"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.InteractOwnPost,)

    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]
    pagination_class = FivePaginationLimitOffset

    def perform_create(self, serializer):
        # Save the currently loggedin user
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetPostSerializer

        return PostSerializer


class PostTagViewset(viewsets.ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer


class PostTagRelationViewset(viewsets.ModelViewSet):
    queryset = PostTagRelation.objects.all()
    serializer_class = PostTagRelationSerializer


class GetImageListAPIView(generics.ListAPIView):
    queryset = PostImages.objects.all()
    pagination_class = FivePaginationLimitOffset

    def get_queryset(self):
        queryset = PostImages.objects.filter(post_id=self.kwargs["pk"])
        return queryset
    serializer_class = PostImagesSerializer
