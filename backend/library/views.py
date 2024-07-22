from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Reader
from .serializers import BookSerializer, ReaderDetailSerializer
from django.utils import timezone
from datetime import timedelta

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        book = self.get_object()
        reader_id = request.data.get('reader_id')
        if not book.is_available:
            return Response({'error': 'Book already checked out'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            reader = Reader.objects.get(id=reader_id)
        except Reader.DoesNotExist:
            return Response({'error': 'Reader not found'}, status=status.HTTP_404_NOT_FOUND)
        book.check_out(reader)
        return Response({'status': 'Book checked out'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def uncheckout(self, request, pk=None):
        book = self.get_object()
        if book.is_available:
            return Response({'error': 'Book is not checked out'}, status=status.HTTP_400_BAD_REQUEST)
        book.return_book()
        return Response({'status': 'Book returned'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def expired_books(self, request):
        now = timezone.now()
        expired_books = Book.objects.filter(expiration_date__lt=now, is_available=False)
        serializer = BookSerializer(expired_books, many=True)
        return Response(serializer.data)


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderDetailSerializer
