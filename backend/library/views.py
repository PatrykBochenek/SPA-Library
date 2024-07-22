from rest_framework import viewsets
from .models import Book, Reader
from .serializers import BookSerializer, ReaderSerializer, ReaderDetailSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderDetailSerializer
