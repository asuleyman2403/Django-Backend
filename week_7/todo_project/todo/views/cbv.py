from todo.models import TodoList, Todo
from todo.serializers import TodoListSerializer, TodoSerializer
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class TodoListsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TodoList.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoListsTodosViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET', 'POST'], detail=False)
    def todos(self):
        try:
            todo_list = TodoList.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except TodoList.DoesNotExist:
            raise Http404
        return todo_list.todo_set.all()


class TodoViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Todo.objects.all()
