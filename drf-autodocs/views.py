from django.views.generic.base import TemplateView
from .parser import TreeAPIParser


class AutoDocsView(TemplateView):

    template_name = "rest_framework_docs/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['endpoints_tree'] = TreeAPIParser().endpoints_tree.to_dict()
        return context
