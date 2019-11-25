from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from user.models import User, Interest
from interest.api.serializers import InterestSerializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    interests = InterestSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'interests')
