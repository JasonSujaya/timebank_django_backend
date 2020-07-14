from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfilesView, AddressViewSet, UserLoginApiView, UserAccountViewset, UserLogoutApiView

router = DefaultRouter()
router.register('userprofile', UserProfilesView,
                base_name='userprofile')
router.register('address', AddressViewSet,
                base_name='address')
router.register('useraccount', UserAccountViewset,
                base_name='useraccount')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),
    path('logout/', UserLogoutApiView.as_view()),

]
