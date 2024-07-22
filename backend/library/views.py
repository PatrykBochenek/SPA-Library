from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Reader
from .serializers import BookSerializer, ReaderDetailSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        book = self.get_object() 
        reader_id = request.data.get('reader_id') 

        if not book.is_available:
            return Response({'detail': 'Book is already checked out.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            reader = Reader.objects.get(id=reader_id)
        except Reader.DoesNotExist:
            return Response({'detail': 'Reader not found.'}, status=status.HTTP_404_NOT_FOUND)

        book.readers.add(reader)
        book.is_available = False  
        book.save() 

        return Response({'detail': 'Book checked out successfully.'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def uncheckout(self, request, pk=None):
        book = self.get_object()
        if book.is_available:
            return Response({'error': 'Book is not checked out'}, status=status.HTTP_400_BAD_REQUEST)
        book.is_available = True
        book.readers.clear()
        book.save()
        return Response({'status': 'Book unchecked out'}, status=status.HTTP_200_OK)

class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderDetailSerializer
