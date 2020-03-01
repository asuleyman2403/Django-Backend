from todo.models import TodoList, Todo
from todo.serializers import TodoListSerializer, TodoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class TodoListsAPIView(generics.ListCreateAPIView):
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TodoList.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoListAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TodoList.objects.for_user(user=self.request.user)


class TodoListTodosAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            todo_list = TodoList.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except TodoList.DoesNotExist:
            raise Http404
        return todo_list.todo_set.all()

    def perform_create(self, serializer):
        try:
            todo_list = TodoList.objects.get(id=self.kwargs['pk'])
        except TodoList.DoesNotExist:
            raise Http404
        serializer.save(list=todo_list)


class TodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Todo.objects.all()
