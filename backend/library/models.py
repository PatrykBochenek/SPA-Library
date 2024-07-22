from django.db import models

class Reader(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    reader = models.ForeignKey(Reader, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
