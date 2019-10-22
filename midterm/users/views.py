from rest_framework import viewsets
from rest_framework import mixins

from users.models import MainUser
from users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return MainUser.objects.all()


