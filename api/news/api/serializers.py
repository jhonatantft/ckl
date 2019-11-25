from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from news.models import News

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
