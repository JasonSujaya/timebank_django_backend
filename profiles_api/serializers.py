from rest_framework import serializers
from .models import UserProfile, Address, ProfileImage
from timebanking_api import models as timebanking_model
import json


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        Address.objects.create(user=user)
        timebanking_model.CurrentBalance.objects.create(user=user)

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class AddressSerializer(serializers.ModelSerializer):
    """Serializes Address for our users"""
    # user = UserProfileSerializer(required=False)

    class Meta:
        model = Address
        fields = "__all__"
        extra_kwargs = {'user': {'read_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes UserProfile for our API"""
    address = AddressSerializer()

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'first_name',
                  'last_name', 'about_me', 'header', 'gender', 'address')
        extra_kwargs = {'email': {'read_only': True}}
        # extra_kwargs = {'address': {'read_only': True}}

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.first_name)
        instance.full_name = str(validated_data.get(
            "first_name", instance.first_name) + " " + validated_data.get(
            "last_name", instance.first_name))
        instance.gender = validated_data.get("gender", instance.gender)
        instance.about_me = validated_data.get("about_me", instance.about_me)
        instance.header = validated_data.get("header", instance.header)
        instance.full_information = str(validated_data.get(
            "about_me", instance.about_me) + validated_data.get("header", instance.header))
        instance.save()

        # Updates or create the address information
        address_data = dict(validated_data.get('address'))
        address = Address.objects.get(user=instance.id)
        address.street = address_data['street']
        address.city = address_data['city']
        address.post_code = address_data['post_code']
        address.save()

        return instance


class ProfileImage(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = "__all__"
        extra_kwargs = {'user_profile': {'read_only': True}}
