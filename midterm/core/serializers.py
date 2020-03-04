from rest_framework import serializers
from core.models import Book, Journal
from core.models import TYPES


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def validate_num_pages(self, value):
        if value < 0:
            raise serializers.ValidationError('Page number must be non-negative')
        return value


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

    def validate_types(self, value):
        if value in [1, 2, 3, 4]:
            return value
        raise serializers.ValidationError('Types must be from 1 to 4')
