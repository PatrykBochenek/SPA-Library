from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta

from .models import Book, Reader
from .serializers import BookSerializer, ReaderSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        book = self.get_object()
        if not book.is_available:
            return Response({'detail': 'Book is not available.'}, status=status.HTTP_400_BAD_REQUEST)

        reader_id = request.data.get('reader_id')
        if not reader_id:
            return Response({'detail': 'Reader ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        reader = Reader.objects.filter(id=reader_id).first()
        if not reader:
            return Response({'detail': 'Reader not found.'}, status=status.HTTP_404_NOT_FOUND)

        book.check_out(reader)
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def uncheckout(self, request, pk=None):
        book = self.get_object()
        if book.is_available:
            return Response({'detail': 'Book is already available.'}, status=status.HTTP_400_BAD_REQUEST)

        book.return_book()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def request(self, request, pk=None):
        book = self.get_object()
        reader_id = request.data.get('reader_id')
        reader = Reader.objects.filter(id=reader_id).first()
        
        if not reader:
            return Response({'error': 'Reader not found'}, status=status.HTTP_400_BAD_REQUEST)

        if book.requested_by:
            return Response({'error': 'Book already requested'}, status=status.HTTP_400_BAD_REQUEST)

        book.requested_by = reader
        book.save()

        serializer = self.get_serializer(book)
        return Response(serializer.data)

class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
