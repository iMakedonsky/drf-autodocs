from inspect import getdoc


def document_serializer_classes(serializer_class, response_serializer_class=None):
    """
    Decorator to make functional view documentable via drf-autodocs
    """
    def decorator(func):
        func.cls.serializer_class = serializer_class
        func.view_class.serializer_class = serializer_class
        if response_serializer_class:
            func.cls.response_serializer_class = response_serializer_class
            func.view_class.response_serializer_class = response_serializer_class
        return func

    return decorator


def format_docstring(*args, **kwargs):
    """
    Decorator for clean docstring formatting
    """
    def decorator(func):
        func.__doc__ = getdoc(func).format(*args, **kwargs)
        return func
    return decorator
