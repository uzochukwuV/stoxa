
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model= User
        fields=['id', 'username', 'password', 'email', 'user_account']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta(object):
        model= UserAccount
        fields=['id', 'total_deposited', 'total_withdrawn', 'stake', 'trade', 'plan_bonus', 'isPremium', 'isVerified', 'owner']

    def create(self, validated_data):
        person = UserAccount.objects.create(
            **validated_data
        )
        return person


