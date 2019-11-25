from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from app.models import App
from .serializers import AppSerializer

class AppsViewSet(ModelViewSet):
    serializer_class = AppSerializer

    queryset = App.objects.all()
