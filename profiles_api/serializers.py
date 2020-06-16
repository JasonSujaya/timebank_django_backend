from rest_framework import serializers
from .models import UserProfile, Address, ProfileImage


class AddressSerializer(serializers.ModelSerializer):
    """Serializes Address for our users"""
    # user = UserProfileSerializer(required=False)

    class Meta:
        model = Address
        fields = "__all__"
        extra_kwargs = {'user_profile': {'read_only': True}}


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
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes UserProfile for our API"""
    address = AddressSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'first_name',
                  'last_name', 'gender', 'password', 'address')
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
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileImage(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = "__all__"
        extra_kwargs = {'user_profile': {'read_only': True}}
