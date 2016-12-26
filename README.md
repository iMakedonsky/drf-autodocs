# Django REST framework auto docs
DRF Auto Docs is an extension of [drf-docs](https://github.com/manosim/django-rest-framework-docs).
In addition to [drf-docs](https://github.com/manosim/django-rest-framework-docs) features provides:

 * optional response fields(if input is different from output)
 * tree-like structure
 * preserves formatting(spaces & new lines) in docstrings
 * markdown in docstrings
 * choice field options
 * specify MethodField output type for docs

# Examples
![drf-autodocs](http://joxi.net/VrwzKWSO8BOkAX.jpg)

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


# Usage

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

# Customization
To change application look & feel, override

`templates/drf_autodocs/index.html`


For additional parsers(if you want other structure than tree), inherit from

 `drf_autodocs.parser.BaseAPIParser`



### Supports
  - Python (3.4, 3.5)
  - Django (1.8, 1.9, 1.10)
  - Django Rest Framework (3+)


# Credits
Thanks to [django](http://djangoproject.com), [django-REST](http://www.django-rest-framework.org/) for their awesome work,
and [drf-docs](https://github.com/manosim/django-rest-framework-docs) for source of inspiration as well as some parts of code