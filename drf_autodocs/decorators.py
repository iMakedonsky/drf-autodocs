from inspect import getdoc


def document_func_view(serializer_class=None,
                       response_serializer_class=None,
                       filter_backends=None,
                       permission_classes=None,
                       authentication_classes=None,
                       doc_format_args=list(),
                       doc_format_kwargs=dict()):
    """
    Decorator to make functional view documentable via drf-autodocs
    """
    def decorator(func):
        if serializer_class:
            func.cls.serializer_class = func.view_class.serializer_class = serializer_class
        if response_serializer_class:
            func.cls.response_serializer_class = func.view_class.response_serializer_class = response_serializer_class
        if filter_backends:
            func.cls.filter_backends = func.view_class.filter_backends = filter_backends
        if permission_classes:
            func.cls.permission_classes = func.view_class.permission_classes = permission_classes
        if authentication_classes:
            func.cls.authentication_classes = func.view_class.authentication_classes = authentication_classes
        if doc_format_args or doc_format_kwargs:
            func.cls.__doc__ = func.view_class.__doc__ = getdoc(func).format(*doc_format_args, **doc_format_kwargs)
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
