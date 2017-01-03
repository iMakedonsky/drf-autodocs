# Django REST framework auto docs
### What is it
DRF Auto Docs is an extension of [drf-docs](https://github.com/manosim/django-rest-framework-docs).
In addition to [drf-docs](https://github.com/manosim/django-rest-framework-docs) features provides:

 * functional view docs
 * tree-like structure
 * Docstrings:
  * markdown
  * preserve space & newlines
  * formatting with nice syntax
 * Fields:
  * choices rendering
  * help_text (to specify SerializerMethodField output, etc)
  * smart read_only/required rendering
 * Endpoint properties:
  * filter_backends
  * authentication_classes
  * permission_classes
  * extra url params(GET params)

### What isn't supported yet:

 * viewsets
 * possibility to try in browser

### Why use this?

 * generates almost whole documentation from your code
 * fills those nasty gaps, that made django-rest-swagger/drf-docs unusable in practice


# Samples

#### Whole structure:

![whole structure](http://joxi.ru/52aBGNI4k3oyA0.jpg)

#### Single node:

![single node](http://joxi.ru/L21G7pT80y9drX.jpg)

#### Choices:

![choices](http://joxi.ru/zAN6KpuBjzP4A9.jpg)

#### Nested items:

![nested items](http://joxi.ru/BA0GynTJp7DB2y.jpg)

#### Help text:

![help text](http://joxi.ru/MAjBv7I4kKQjAe.jpg)

#### Docstring formatting:
```python
@format_docstring(request_example, response_example=response_example)
class BookReadUpdateHandler(RetrieveUpdateAPIView):
    """
    Wow, this magic decorator allows us to:
        1) Keep clean & short docstring
        2) Insert additional data in it, like request/response examples

    Request: {}
    Response: {response_example}
    """
```
![help text](http://joxi.ru/VrwzKWSO4YekAX.jpg)


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

### Tree-like structure

Tree-like structure is built from url prefixes. To make your endpoints grouped by some
category, you must include your urls within other url. There are, generally, 2 ways to achieve it:

Example 1:

```python
university_urlpatterns = [
    url(r'^lecturers/', university_views.LecturersHandler.as_view(), name='lecturers'),
    url(r'^lecturers/(?P<pk>\d+)/$', university_views.LecturerUpdateHandler.as_view(), name='lecturer_read_update'),
    url(r'^universities/', university_views.UniversitiesHandler.as_view(), name='universities'),
]

urlpatterns = [
    url(r'^library/', include(library_urlpatterns, namespace='library')),
    url(r'^university/', include(university_urlpatterns, namespace='university')),
]
```

Example 2:
```python
urlpatterns = [
    url(r'^library/', include(library_urlpatterns, namespace='library')),
    url(r'^university/', include([
        url(r'^lecturers/', university_views.LecturersHandler.as_view(), name='lecturers'),
        url(r'^lecturers/(?P<pk>\d+)/$', university_views.LecturerUpdateHandler.as_view(), name='lecturer_read_update'),
        url(r'^universities/', university_views.UniversitiesHandler.as_view(), name='universities')
    ], namespace='university')),
]
```


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

### Function-based views

For functional views, decorate them with.

`drf_autodocs.decorators.document_func_view`

Now you can insert into view via kwargs:

 * serializer_class
 * response_serializer_class
 * filter_backends
 * authentication_classes
 * permission_classes
 * doc_format_args
 * doc_format_kwargs

Now it should look like:
```python
from drf_autodocs.decorators import document_func_view

format_args = ['"This string\nwas inserted"',]

@document_func_view(serializer_class=BookSerializer,
                    response_serializer_class=LibrarySerializer,
                    doc_format_args=format_args)
@api_view(['GET', 'POST', 'DELETE'])
def hello_world(request):
    """
    Works for `functional` views too!
        Yeah, that thing rocks!
        And allows formatting {}
    """
    return Response('hello_world response')
```

### Help text

This package uses default DRF field attribute `help_text`
If you're using `ModelSerializer`, and model field got `help_text` attr, it will be
transferred to your serializers' field automatically.

Example:

```python
has_books = serializers.SerializerMethodField(help_text='returns Bool')
```

### Docstring formatting

```python
from .request_response_examples import request_example, response_example
from drf_autodocs.decorators import format_docstring


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
```


### Extra URL(GET) parameters
Please think twice before using such parameters, as they might be unneeded.

But if you really need them, here you go:

```python
class LibrariesHandler(ListCreateAPIView):
    """
    Shiny and nice docstring, which:
        1) allows formatting
        2) `allows markdown`
    """
    extra_url_params = (('show_all', 'Bool', 'if True returns all instances and only 5 otherwise'),
                        ('some_extra_param', 'Integer', 'Something more to be included there'))
```

Results in:

![extra_url_params](http://joxi.ru/E2ppYWh9GMzJ2Y.jpg)

# Customization
To change application look & feel, override templates and/or static files.

Root template is :
`templates/drf_autodocs/index.html`


For additional parsers(if you want other structure than tree), inherit from

 `drf_autodocs.parser.BaseAPIParser`



### Supports
  - Python 3(Not tested on 2, though might work)
  - Django 1.8+
  - Django Rest Framework 3+


# Credits
Thanks to [django](http://djangoproject.com), [django-REST](http://www.django-rest-framework.org/) for their awesome work,
and [drf-docs](https://github.com/manosim/django-rest-framework-docs) for source of inspiration as well as some parts of code.


Developed with care by Mashianov Oleksander at

[![buddhasoft](http://i63.tinypic.com/2h87nzm.png)](http://buddhasoft.net/)


If you :thumbsup: this, don't forget to :star: it and share with friends.