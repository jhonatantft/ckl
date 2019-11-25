from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from interest.models import Interest
from .serializers import InterestSerializer

class InterestsViewSet(ModelViewSet):
    serializer_class = InterestSerializer

    queryset = Interest.objects.all()
