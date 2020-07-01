from rest_framework import serializers
from .models import CurrentBalance, Transaction, TransactionStatus


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        # extra_kwargs = {'user_profile': {'read_only': True}}


class CurrentBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentBalance
        fields = "__all__"
        # extra_kwargs = {'user_profile': {'read_only': True}}


class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = "__all__"
        # extra_kwargs = {'user_profile': {'read_only': True}}
