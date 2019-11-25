from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from interest.models import Interest

class InterestSerializer(ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'
