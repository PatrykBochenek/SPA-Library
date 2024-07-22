from rest_framework import serializers
from .models import Book, Reader

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    readers = ReaderSerializer(many=True, read_only=True)
    expiration_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'is_available', 'readers', 'checked_out_at', 'expiration_date']
class ReaderDetailSerializer(serializers.ModelSerializer):
    books_taken = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = ['id', 'name', 'books_taken']
