from django.views.generic.base import TemplateView
from .parser import TreeAPIParser


class TreeView(TemplateView):

    template_name = "drf_autodocs/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['endpoints_tree'] = TreeAPIParser().endpoints_tree.to_dict()
        return context
