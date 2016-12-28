# Django REST framework auto docs
### What is it
DRF Auto Docs is an extension of [drf-docs](https://github.com/manosim/django-rest-framework-docs).
In addition to [drf-docs](https://github.com/manosim/django-rest-framework-docs) features provides:

 * optional response fields(if input is different from output)
 * functional view input/output documentation
 * tree-like structure
 * preserves formatting(spaces & new lines) in docstrings
 * markdown in docstrings
 * choice field options
 * fields' help_text (to specify SerializerMethodField output, for example)
 * read_only/required rendering

What isn't supported yet:

 * viewsets
 * possibility to try in browser
 * permission listing
 * tokens
 * content types

Why use this?

 * keeps project and documentation synchronized without any efforts
 * it's as DRY as django/rest_framework themselves



# Samples
Whole structure:

![whole structure](http://joxi.net/LmGnYqhelBEWrl.jpg)


Single node:

![single node](http://joxi.net/E2ppYWh9GvEW2Y.jpg)

Choices:

![choices](http://joxi.net/12M5L7CMkgyb2J.jpg)

Nested items:

![nested items](http://joxi.net/brRK3EhJOBZdm1.jpg)

Help text:

![help text](http://joxi.net/n2YXyRsoekWNm6.jpg)

# Installation
In virtualenv:

    pip install drf_autodocs

In settings:

    INSTALLED_APPS = [
        ...
        'drf_autodocs',
        ...
    ]

In your urls:

    urlpatterns = [
        ...
        url(r'^', include('drf_autodocs.urls')),
    ]


That's already enough for swagger-like docs,
result available on

`localhost:8000/docs/`

If you want functional views support and some more features, read below.

# Usage

### Class-Based views
Say you have a view like this:
```python
class BookReadUpdateHandler(RetrieveUpdateAPIView):
    serializer_class = BookUpdateSerializer
    queryset = Book.objects.all()
```

And say this serializers' input is different from output:
```python
class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'author')
        model = Book

    def to_representation(self, instance):
        return LibrarySerializer(instance.library)
```

Now to know what return format is, one must make a request.
This package simplifies it via:

`response_serializer_class = YourSerializer`

Now your view looks like:
```python
class BookReadUpdateHandler(RetrieveUpdateAPIView):
    """
    Shiny and nice docstring, which:
        1) allows formatting
        2) `allows markdown`
    """
    serializer_class = BookUpdateSerializer
    response_serializer_class = LibrarySerializer
    queryset = Book.objects.all()
```

###Function-based views
For functional views, decorate them with.

`drf_autodocs.decorators.document_serializer_classes`

Note that response_serializer_class is optional.

Now it should look like
```python
from drf_autodocs.decorators import document_serializer_classes

@document_serializer_classes(serializer_class=BookSerializer, response_serializer_class=LibrarySerializer)
@api_view(['GET', 'POST', 'DELETE'])
def hello_world(request):
    """
    Works for `functional` views too!
    Yeah, that thing rocks!
    """
    return Response('hello_world response')
```


# Customization
To change application look & feel, override

`templates/drf_autodocs/index.html`


For additional parsers(if you want other structure than tree), inherit from

 `drf_autodocs.parser.BaseAPIParser`



### Supports
  - Python 3(Not tested on 2, though might work)
  - Django 1.8+
  - Django Rest Framework 3+


# Credits
Thanks to [django](http://djangoproject.com), [django-REST](http://www.django-rest-framework.org/) for their awesome work,
and [drf-docs](https://github.com/manosim/django-rest-framework-docs) for source of inspiration as well as some parts of code