from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionView, CurrentBalanceView, TransactionStatusView

router = DefaultRouter()
router.register('transactions', TransactionView,
                base_name='transactions')
router.register('balance', CurrentBalanceView,
                base_name='balance')
router.register('status', TransactionStatusView,
                base_name='status')

urlpatterns = [
    path('', include(router.urls)),
]
