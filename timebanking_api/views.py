from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins

# Import Apps & Serializers
from .models import CurrentBalance, Transaction, TransactionStatus
from .serializers import CurrentBalanceSerializer, TransactionSerializer, TransactionStatusSerializer
from Timeo_Project.pagination import FivePaginationLimitOffset

# Create your views here.


class TransactionView(viewsets.ModelViewSet):
    """Handles creating and fetching profile"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = FivePaginationLimitOffset

    def perform_create(self, serializer):
        # Save the currently loggedin user
        serializer.save(sender=self.request.user)


class CurrentBalanceView(viewsets.ModelViewSet):
    """Handles creating and fetching profile"""
    queryset = CurrentBalance.objects.all()
    serializer_class = CurrentBalanceSerializer
    pagination_class = FivePaginationLimitOffset


class TransactionStatusView(viewsets.ModelViewSet):
    """Handles creating and fetching profile"""
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer
