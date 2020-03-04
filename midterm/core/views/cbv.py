from rest_framework import mixins, viewsets
from core.serializers import BookSerializer, JournalSerializer
from core.models import Book, Journal
from rest_framework.permissions import AllowAny, IsAuthenticated


class BooksAPIView(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
    #         permission_classes = [IsAuthenticated]
    #     if self.action == 'list' or self.action == 'retrieve':
    #         permission_classes = [IsAuthenticated]
    #     return permission_classes


class JournalsAPIView(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
    #         permission_classes = [IsAuthenticated]
    #     if self.action == 'list' or self.action == 'retrieve':
    #         permission_classes = [IsAuthenticated]
    #     return permission_classes
