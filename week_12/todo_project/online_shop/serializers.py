from rest_framework import serializers
from online_shop.models import Category, Product
from my_auth.serializers import MyUserSerializer


class CategoryBaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'created_at')


class CategorySerializer(CategoryBaseSerializer):
    owner = MyUserSerializer(required=False)

    class Meta(CategoryBaseSerializer.Meta):
        model = Category
        fields = CategoryBaseSerializer.Meta.fields + ('owner',)


class ProductBaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.IntegerField(required=True)
    price = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'status', 'price')


class ProductSerializer(ProductBaseSerializer):
    category = CategorySerializer(required=False)
    image = serializers.ImageField(required=False)

    class Meta(ProductBaseSerializer.Meta):
        fields = ProductBaseSerializer.Meta.fields + ('category', 'image',)

