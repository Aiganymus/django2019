from django.db import transaction
from rest_framework import serializers

from users.models import Profile, MainUser


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone', 'address')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = MainUser
        fields = '__all__'

    def create(self, validated_data):
        with transaction.atomic():
            profile_data = validated_data.pop('profile')
            user = MainUser.objects.create(**validated_data)
            Profile.objects.create(user=user, **profile_data)
            return user
