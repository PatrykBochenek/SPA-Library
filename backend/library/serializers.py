from rest_framework import serializers
from .models import Book, Reader

class BookSerializer(serializers.ModelSerializer):
    readers = serializers.SerializerMethodField()
    expiration_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    requested_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'is_available', 'readers', 'checked_out_at', 'expiration_date', 'requested_by']

    def get_readers(self, obj):
        return [{'id': reader.id, 'name': reader.name} for reader in obj.readers.all()]

class ReaderSerializer(serializers.ModelSerializer):
    books_taken = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = ['id', 'name', 'books_taken']

class ReaderDetailSerializer(serializers.ModelSerializer):
    books_taken = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = ['id', 'name', 'books_taken']
