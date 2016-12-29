from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_autodocs.decorators import format_docstring


from .serializers import (
    BookSerializer,
    BookUpdateSerializer,
    LibrarySerializer
)
from .request_response_examples import request_example, response_example
from library.models import Book, Library


# works for badly-designed views too
class BooksHandler(APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=200, data="This works for bad-designed views too!")


@format_docstring(request_example, response_example=response_example)
class BookReadUpdateHandler(RetrieveUpdateAPIView):
    """
    Wow, this magic decorator allows us to:
        1) Keep clean & short docstring
        2) Insert additional data in it, like request/response examples

    Request: {}
    Response: {response_example}
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


