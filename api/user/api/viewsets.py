from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from user.models import User
from .serializers import UserSerializer

class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer

    queryset = User.objects.all()
