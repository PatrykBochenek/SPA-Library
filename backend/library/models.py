# myapp/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True) 
    readers = models.ManyToManyField('Reader', related_name='books_taken', blank=True) 

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def has_taken_out(self, book):
        return book in self.books_taken.all()
