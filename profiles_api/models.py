from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import datetime

from django.conf import settings
from django.utils import timezone
from phone_field import PhoneField
from django.conf import settings
# Create user model


class MyUserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Models In The System"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.date.today)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    is_active = models.BooleanField(default=True)
    notification_newsletter = models.BooleanField(default=True)
    notifictioon_post = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.datetime.now)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', "last_name"]

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between"""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        """Returns the first name """
        return self.first_name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class Address(models.Model):
    user_profile = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    post_code = models.CharField(max_length=255, null=True)

    def __str__(self):
        """Return string representation of address"""
        return self.street


class ProfileImage(models.Model):
    user_profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, primary_key=True)
    image_path = models.ImageField(blank=False, null=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        """Return string representation of address"""
        return self.street
