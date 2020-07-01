from django.contrib import admin
from .models import UserProfile, Address, ProfileImage, UserConsent, Gender, UserStatus

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(UserStatus)
admin.site.register(UserConsent)
admin.site.register(ProfileImage)
admin.site.register(Gender)
