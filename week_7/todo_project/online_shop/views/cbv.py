from online_shop.models import Category, Product
from online_shop.serializers import CategorySerializer, ProductSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.http import Http404


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryProductsViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET', 'POST'], detail=False)
    def products(self):
        try:
            category = Category.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            raise Http404
        return category.product_set.all()


class ProductsViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Product.objects.all()
