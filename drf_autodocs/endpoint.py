from rest_framework.serializers import BaseSerializer, ChoiceField, RelatedField, ManyRelatedField
from rest_framework.filters import SearchFilter
from inspect import getdoc
from django.contrib.admindocs.views import simplify_regex
from drf_autodocs import builtin_docs
from django.conf import settings


class Endpoint:
    counter = 0

    def __init__(self, pattern, prefix=None):
        self.id = Endpoint.counter
        Endpoint.counter += 1

        self.pattern = pattern
        self.view = pattern.callback
        self.methods = self._get_allowed_methods()
        self.complete_path = self._get_complete_path(pattern, prefix)

        self.name = self._get_endpoint_name()

        if hasattr(self.view.cls, 'extra_url_params'):
            self.extra_url_params = self.view.cls.extra_url_params

        if hasattr(self.view.cls, 'filter_backends') and len(getattr(self.view.cls, 'filter_backends')) > 0:
            self._collect_filter_backends()

        if hasattr(self.view.cls, 'authentication_classes') and self.view.cls.authentication_classes is not None:
            self.authentication_classes = [(cls.__name__, getdoc(cls)) for cls in self.view.cls.authentication_classes]

        if hasattr(self.view.cls, 'permission_classes') and self.view.cls.permission_classes is not None:
            self.permission_classes = [(cls.__name__, getdoc(cls)) for cls in self.view.cls.permission_classes]

        self.docstring = getdoc(self.view.cls)

        if hasattr(self.view.cls, 'serializer_class') and self.view.cls.serializer_class is not None:
            self.input_fields = self._get_serializer_fields(self.view.cls.serializer_class())

        if hasattr(self.view.cls, 'response_serializer_class'):
            self.output_fields = self._get_serializer_fields(self.view.cls.response_serializer_class())

    def _get_endpoint_name(self):
        if hasattr(settings, 'AUTODOCS_ENDPOINT_NAMES') and settings.AUTODOCS_ENDPOINT_NAMES == 'view':
            ret = ''.join(
                [
                    (' %s' % c if c.isupper() and not self.view.__name__.startswith(c) else c)
                    for c in self.view.__name__
                    ]
            ).replace('-', ' ').replace('_', ' ').title()
            return ret
        else:
            return self.pattern.name.replace('-', ' ').replace('_', ' ').title()

    def _collect_filter_backends(self):
        self.filter_backends = []
        for f in self.view.cls.filter_backends:
            if f in builtin_docs.filter_backends:
                if f is SearchFilter:
                    if hasattr(self.view.cls, 'search_filters'):
                        doc = builtin_docs.filter_backends[f](self.view.cls.search_filters)
                    else:
                        doc = "Developer didn't specify any fields for search"
                else:
                    doc = builtin_docs.filter_backends[f]
                self.filter_backends.append((f.__name__, doc))
            else:
                self.filter_backends.append((f.__name__, getdoc(f)))

    def _get_allowed_methods(self):
        if hasattr(self.view, 'cls'):
            return [m.upper() for m in self.view.cls.http_method_names if hasattr(self.view.cls, m)]
        else:
            return []

    @staticmethod
    def _get_complete_path(pattern, prefix=None):
        return prefix + simplify_regex(pattern._regex)

    def _get_serializer_fields(self, serializer):
        fields = []

        if hasattr(serializer, 'get_fields'):
            for key, field in serializer.get_fields().items():
                to_many_relation = True if hasattr(field, 'many') else False
                sub_fields = []

                if to_many_relation:
                    sub_fields = self._get_serializer_fields(field.child) if isinstance(field, BaseSerializer) else None
                else:
                    sub_fields = self._get_serializer_fields(field) if isinstance(field, BaseSerializer) else None
                field_data = {
                    "name": key,
                    "read_only": field.read_only,
                    "type": str(field.__class__.__name__),
                    "sub_fields": sub_fields,
                    "required": field.required,
                    "to_many_relation": to_many_relation,
                    "help_text": field.help_text,
                    "write_only": field.write_only
                }
                if isinstance(field, ChoiceField) and not isinstance(field, (RelatedField, ManyRelatedField)):
                    field_data['choices'] = field.choices

                if isinstance(field, RelatedField):
                    field_data['help_text'] = ('{}\nRequires/renders pk(id) of {} as integer'.format(
                        field.help_text if field.help_text else "",
                        field.queryset.model.__name__)
                    )
                elif isinstance(field, ManyRelatedField):
                    field_data['help_text'] = ("{}\nRequires/renders list of pk's(id's) of {} objects.".format(
                        field.help_text if field.help_text else "",
                        field.child_relation.queryset.model.__name__)
                    )

                fields.append(field_data)

        return fields





