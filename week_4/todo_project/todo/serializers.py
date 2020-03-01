from rest_framework import serializers
from todo.models import TodoList, Todo
from my_auth.serializers import MyUserSerializer


class TodoListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = MyUserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'owner', 'created_at')


class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    list = TodoListSerializer(required=False)
    status = serializers.IntegerField(required=True)

    class Meta:
        model = Todo
        fields = ('id', 'name', 'list', 'status')

