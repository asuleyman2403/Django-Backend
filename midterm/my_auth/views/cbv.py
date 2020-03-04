from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from my_auth.serializers import MyUserSerializer
from my_auth.models import MyUser


class MyUserAPIView(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()

