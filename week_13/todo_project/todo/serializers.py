from rest_framework import serializers
from todo.models import TodoList, Todo
from my_auth.serializers import MyUserSerializer


class TodoListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = MyUserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)
    task_amount = serializers.IntegerField(required=False)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'owner', 'created_at', 'task_amount')


class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    list = TodoListSerializer(required=False)
    status = serializers.IntegerField(required=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Todo
        fields = ('id', 'name', 'list', 'status', 'image')

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

