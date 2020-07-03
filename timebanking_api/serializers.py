from rest_framework import serializers
from .models import CurrentBalance, Transaction, TransactionStatus

from django.db import transaction
from django.utils import timezone


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ('sender', 'created_date')

    def create(self, validated_data):
        user = self.context['request'].user
        time_limit = timezone.now() - timezone.timedelta(minutes=5)
        transaction_list = Transaction.objects.filter(sender=user, created_date__range=[
            time_limit, timezone.now(), ])

        # prevent creation of more than 5 post under 5 minutes
        if (transaction_list.count() <= 5):
            sending_money = Transaction.objects.create(**validated_data)
            with transaction.atomic():
                balance_sender = CurrentBalance.objects.select_for_update().get(
                    user=self.context['request'].user.id)
                balance_receiver = CurrentBalance.objects.select_for_update().get(
                    user=validated_data["receiver"])
                if(balance_sender.amount >= validated_data["value"]):
                    balance_sender.amount -= validated_data["value"]
                    balance_receiver.amount += validated_data["value"]
                    balance_sender.save()
                    balance_receiver.save()
                    return sending_money
                else:
                    print("account balance is not sufficient")
                    pass
        else:
            print("Too much Transaction ERROR")
            pass

    # sender = models.ForeignKey(
    #     profiles_models.UserProfile, related_name="user_from_transaction", on_delete=models.SET_NULL, null=True)
    # receiver = models.ForeignKey(
    #     profiles_models.UserProfile, related_name="user_to_id", on_delete=models.SET_NULL, null=True)
    # value = models.PositiveIntegerField(default=0)
    # status = models.ForeignKey(
    #     TransactionStatus, on_delete=models.SET_NULL, null=True)


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
