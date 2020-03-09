from rest_framework import serializers
from online_shop.models import Category, Product
from my_auth.serializers import MyUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = MyUserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = CategorySerializer(required=False)
    status = serializers.IntegerField(required=True)
    price = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'status', 'price')

