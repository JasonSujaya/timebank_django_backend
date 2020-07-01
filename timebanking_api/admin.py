from django.contrib import admin
from .models import CurrentBalance, Transaction, TransactionStatus

# Register your models here.
admin.site.register(CurrentBalance)
admin.site.register(Transaction)
admin.site.register(TransactionStatus)
