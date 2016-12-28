from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    BookSerializer,
    BookUpdateSerializer,
    LibrarySerializer
)
from library.models import Book, Library

from drf_autodocs.decorators import document_serializer_classes


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


@document_serializer_classes(serializer_class=BookSerializer, response_serializer_class=LibrarySerializer)
@api_view(['GET', 'POST', 'DELETE'])
def hello_world(request):
    """
    Works for `functional` views too!
    Yeah, that thing rocks!
    """
    return Response('hello_world response')


