from rest_framework import serializers
from my_auth.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')
