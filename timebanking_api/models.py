from django.db import models
from profiles_api import models as profiles_models
from post_api import models as post_api_models

# Create your models here.


class CurrentBalance(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, related_name="user_balance", on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.post_id.title


class TransactionStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Transaction(models.Model):
    user_from_id = models.ForeignKey(
        profiles_models.UserProfile, related_name="user_from_transaction", on_delete=models.CASCADE)
    user_to_id = models.ForeignKey(
        profiles_models.UserProfile, related_name="user_to_id", on_delete=models.CASCADE)
    value = models.IntegerField()
    transaction_status = models.OneToOneField(
        TransactionStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_id.title
