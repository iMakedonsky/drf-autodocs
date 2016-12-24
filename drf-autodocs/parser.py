from django.conf import settings
from importlib import import_module
from django.utils.module_loading import import_string
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from addict import Dict
from rest_framework.views import APIView
from .endpoint import Endpoint


class APIParser:

    def __init__(self, patterns=None):
        self.patterns = patterns
        if not patterns:
            try:
                root_urlconf = import_string(settings.ROOT_URLCONF)
            except ImportError:
                # Handle a case when there's no dot in ROOT_URLCONF
                root_urlconf = import_module(settings.ROOT_URLCONF)
            if hasattr(root_urlconf, 'urls'):
                self.patterns = root_urlconf.urls.urlpatterns
            else:
                self.patterns = root_urlconf.urlpatterns
        self.parse()

    def parse(self):
        raise NotImplementedError("Inherit some parser from this class first")

    @staticmethod
    def _is_drf_pattern(pattern):
        return isinstance(pattern.callback, APIView)


class TreeAPIParser(APIParser):
    """
    Creates a nice tree of API
    """
    def __init__(self, *args, **kwargs):
        self.endpoints_tree = Dict()
        super().__init__(*args, **kwargs)

    def parse(self):
        self.parse_tree(self.patterns, self.endpoints_tree)

    def parse_tree(self, urlpatterns, parent_node):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver):
                child_node_name = pattern.app_name or pattern._regex.replace('^', '').replace('/', '').replace('$', '')
                parent_node[child_node_name] = Dict()
                self.parse_tree(
                    urlpatterns=pattern.url_patterns,
                    parent_node=parent_node[child_node_name]
                )
            elif isinstance(pattern, RegexURLPattern) and self._is_drf_pattern(pattern):
                api_endpoint = Endpoint(pattern)
                parent_node[api_endpoint.path] = api_endpoint







