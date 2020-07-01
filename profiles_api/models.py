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
        user = self.create_user(email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserStatus(models.Model):
    status = models.CharField(max_length=255, null=True)

    def __str__(self):
        """Return string representation of address"""
        return self.status


class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of address"""
        return self.name


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Models In The System"""
    gender = models.ForeignKey(
        Gender, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(
        UserStatus, on_delete=models.SET_NULL, null=True)

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.date.today)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    current_balance = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    notification_newsletter = models.BooleanField(default=True)
    notifictioon_post = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        default=timezone.now)

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


class UserConsent(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    consent_form = models.CharField(max_length=255)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        """Return string representation"""
        return self.user.first_name


class ProfileImage(models.Model):
    user = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, primary_key=True)
    image_path = models.ImageField(null=True)
    title = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        """Return string representation"""
        return self.street


class Country(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        """Return string representation"""
        return self.name


class Address(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    post_code = models.CharField(max_length=255, null=True)

    def __str__(self):
        """Return string representation"""
        return self.street
