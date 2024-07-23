from django.db import models
from datetime import timedelta
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    readers = models.ManyToManyField('Reader', related_name='books_taken', blank=True)
    checked_out_at = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    requested_by = models.ForeignKey('Reader', null=True, blank=True, on_delete=models.SET_NULL, related_name='requested_books')

    def __str__(self):
        return self.title

    def check_out(self, reader):
        self.is_available = False
        self.checked_out_at = timezone.now()
        self.expiration_date = self.checked_out_at + timedelta(days=30)
        self.requested_by = None
        self.save()
        self.readers.add(reader)

    def return_book(self):
        self.is_available = True
        self.checked_out_at = None
        self.expiration_date = None
        self.save()
        self.readers.clear()

class Reader(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def has_taken_out(self, book):
        return book in self.books_taken.all()
