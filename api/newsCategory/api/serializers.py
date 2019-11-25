from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from newsCategory.models import NewsCategory

class NewsCategorySerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'
