from rest_framework import serializers
from .models import Book, Reader

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    readers = ReaderSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'is_available', 'readers']

class ReaderDetailSerializer(serializers.ModelSerializer):
    books_taken = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = ['id', 'name', 'books_taken']
