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
from .serializers import UserProfileSerializer, AddressSerializer, UserAccountSerializer
from .models import UserProfile, Address

from Timeo_Project.pagination import FivePaginationLimitOffset


class UserAccountViewset(viewsets.ModelViewSet):
    """Handles Authentication"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    """Handles creating and fetching profile"""
    queryset = UserProfile.objects.all()
    serializer_class = UserAccountSerializer

    pagination_class = FivePaginationLimitOffset


class UserProfilesView(viewsets.ModelViewSet):
    """Handles Authentication"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    """Handles creating and fetching profile"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    pagination_class = FivePaginationLimitOffset

    def create(self, request):
        response = {
            'message': 'Create function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class AddressViewSet(viewsets.ModelViewSet):
    # WILL REMOVE THIS
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
