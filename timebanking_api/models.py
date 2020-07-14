from django.db import models
from profiles_api import models as profiles_models
from post_api import models as post_api_models
from django.utils import timezone
from django.core.validators import MinValueValidator

from django.contrib.postgres.indexes import BrinIndex

# Create your models here.


class CurrentBalance(models.Model):
    user = models.OneToOneField(
        profiles_models.UserProfile, related_name="user_balance", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.amount)


class TransactionStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    sender = models.ForeignKey(
        profiles_models.UserProfile, related_name="user_from_transaction", on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey(
        profiles_models.UserProfile, related_name="user_to_id", on_delete=models.SET_NULL, null=True)
    value = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(1)])
    status = models.ForeignKey(
        TransactionStatus, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.value)

    class Meta:
        indexes = [
            BrinIndex(fields=['created_date']),
        ]
