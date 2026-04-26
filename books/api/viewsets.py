from rest_framework import viewsets

from books.api import serialzers
from books import models

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serialzers.BookSerializer
    queryset = models.Book.objects.all()