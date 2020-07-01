from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins

# Import Apps & Serializers
from .models import CurrentBalance, Transaction, TransactionStatus
from .serializers import CurrentBalanceSerializer, TransactionSerializer, TransactionStatusSerializer

# Create your views here.


class TransactionView(viewsets.ModelViewSet):
    """Handles creating and fetching profile"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CurrentBalanceView(viewsets.ModelViewSet):
    """Handles creating and fetching profile"""
    queryset = CurrentBalance.objects.all()
    serializer_class = CurrentBalanceSerializer


class TransactionStatusView(viewsets.ModelViewSet):
    """Handles creating and fetching profile"""
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer
