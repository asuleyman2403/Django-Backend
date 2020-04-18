from todo.models import TodoList, Todo
from todo.serializers import TodoListSerializer, TodoSerializer
from rest_framework import mixins, viewsets, generics
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

    # @action(methods=['GET'], detail=True, url_path='todos')
    # def get_todos(self, request, pk):
    #     try:
    #         todo_list = TodoList.objects.for_user(user=self.request.user).get(id=pk)
    #     except TodoList.DoesNotExist:
    #         raise Http404
    #     data = list(todo_list.todo_set.all().values())
    #     return JsonResponse(data, safe=False)
    #
    # @action(methods=['POST'], detail=True, url_path='create_todo')
    # def create_todo(self, request, pk):
    #     try:
    #         todo_list = TodoList.objects.for_user(user=self.request.user).get(id=pk)
    #     except TodoList.DoesNotExist:
    #         raise Http404
    #     serializer = TodoSerializer(data=self.request.data)
    #     if serializer.is_valid():
    #         serializer.save(list=todo_list)
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


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
            todo_list = TodoList.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except TodoList.DoesNotExist:
            raise Http404
        serializer.save(list=todo_list)


class TodoViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()

