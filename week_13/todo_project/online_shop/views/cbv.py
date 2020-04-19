from online_shop.models import Category, Product
from online_shop.serializers import CategorySerializer, ProductSerializer
from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

import logging
logger = logging.getLogger('api')


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
        logger.info(f'Category with id = {serializer.data["id"]} created')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Category with id = {serializer.data["id"]} has been updated')


class CategoryProductsAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            category = Category.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            logger.warning(f'Category with id = {self.kwargs["pk"]} not found')
            raise Http404
        return category.product_set.all()

    def perform_create(self, serializer):
        try:
            category = Category.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            logger.warning(f'Category with id = {self.kwargs["pk"]} not found')
            raise Http404
        serializer.save(category=category)
        logger.info(f'Product with id = {serializer.data["id"]} created')


class ProductsViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Product.objects.all()
