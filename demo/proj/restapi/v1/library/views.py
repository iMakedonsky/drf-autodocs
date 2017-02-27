from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from drf_autodocs.decorators import format_docstring


from .serializers import (
    BookUpdateSerializer,
    LibrarySerializer,
    BookSerializer
)
from .request_response_examples import request_example, response_example
from library.models import Book, Library


# works for badly-designed views too
class BooksHandler(ListAPIView):
    """bad-designed view"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


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
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly, DjangoModelPermissions)
    filter_backends = (OrderingFilter, SearchFilter)
    search_filters = ('=name', '$type')
    serializer_class = LibrarySerializer
    extra_url_params = (('show_all', 'Bool', 'if True returns all instances and only 5 otherwise'),
                        ('some_extra_param', 'Integer', 'Something more to be included there'))

    def get_queryset(self):
        if self.request.GET.get('show_all'):
            return Library.objects.all()
        else:
            return Library.objects.all[:5]

