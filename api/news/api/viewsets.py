from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from news.models import News
from .serializers import NewsSerializer

class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer

    queryset = News.objects.all()
