from rest_framework import viewsets

from bored.serializers import UserSerializer
from bored.models import User
from bored.permissions import IsUserOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOnly,)