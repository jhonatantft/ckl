from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from newsCategory.models import NewsCategory
from .serializers import NewsCategorySerializer

class NewsCategoriesViewSet(ModelViewSet):
    serializer_class = NewsCategorySerializer

    queryset = NewsCategory.objects.all()
