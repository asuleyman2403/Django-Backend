from todo.models import TodoList, Todo
from todo.serializers import TodoListSerializer, TodoSerializer
from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
import logging
logger = logging.getLogger('api')


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
        logger.info(f'TodoList with id = {serializer.data["id"]} created')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'TodoList with id = {serializer.data["id"]} has been updated')


class TodoListTodosAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            todo_list = TodoList.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except TodoList.DoesNotExist:
            logger.warning(f'TodoList with id {self.kwargs["pk"]} not found')
            raise Http404
        return todo_list.todo_set.all()

    def perform_create(self, serializer):
        try:
            todo_list = TodoList.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except TodoList.DoesNotExist:
            logger.warning(f'TodoList with id {self.kwargs["pk"]} not found')
            raise Http404
        serializer.save(list=todo_list)
        logger.info(f'Todo Task of Task List {self.kwargs["pk"]} created')


class TodoViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()

