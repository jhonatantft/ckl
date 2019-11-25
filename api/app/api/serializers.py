from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from app.models import App

class AppSerializer(ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
