from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import (
    BookSerializer,
    BookUpdateSerializer,
    LibrarySerializer
)
from library.models import Book, Library


class BooksHandler(ListCreateAPIView):
    """
    Shiny and nice docstring, which:
        1) allows formatting
        2) `allows markdown`
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookReadUpdateHandler(RetrieveUpdateAPIView):
    """
    Shiny and nice docstring, which:
        1) allows formatting
        2) `allows markdown`
    """
    serializer_class = BookUpdateSerializer
    response_serializer_class = LibrarySerializer
    queryset = Book.objects.all()


class LibrariesHandler(ListCreateAPIView):
    """
    Shiny and nice docstring, which:
        1) allows formatting
        2) `allows markdown`
    """
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()


