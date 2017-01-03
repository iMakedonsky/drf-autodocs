from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    BookSerializer,
    BookUpdateSerializer,
    LibrarySerializer
)
from library.models import Book

from drf_autodocs.decorators import document_func_view


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


@document_func_view(serializer_class=BookSerializer, response_serializer_class=LibrarySerializer,
                    doc_format_args=('"This string\nwas inserted"',))
@api_view(['GET', 'POST', 'DELETE'])
def hello_world(request):
    """
    Works for `functional` views too!
    Yeah, that thing rocks!
    And allows formatting {}
    """
    return Response('hello_world response')


