from rest_framework.views import APIView


class Endpoint:

    def __init__(self, pattern):
        self.pattern = pattern
        self.view = pattern.callback.cls
        self.methods = self._get_allowed_methods()
        self.complete_path = self._get_complete_path()

    def _get_allowed_methods(self):
        return [m.upper() for m in self.view.http_method_names if hasattr(self.view.cls, m)]

    def _get_complete_path(self):
        return ""
        # TODO





