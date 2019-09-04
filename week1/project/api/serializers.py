from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CompanySerializer(serializers.ModelSerializer):
    boss = UserSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
