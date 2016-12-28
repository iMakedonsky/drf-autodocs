import markdown
from rest_framework.utils.formatting import markup_description
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeData
from django.utils.text import normalize_newlines
from django.utils.html import escape
from ..endpoint import Endpoint


register = template.Library()


@register.filter(name='markdownify')
@stringfilter
def markdownify(value):
    return markup_description(value)


@register.filter(is_safe=True, needs_autoescape=True, name='keep_formatting')
@stringfilter
def keep_spacing(value, autoescape=None):
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    value = mark_safe(value.replace('  ', ' &nbsp;').replace('\t', '&emsp;'))
    return mark_safe(value.replace('\n', '<br />'))


@register.filter()
def is_endpoint(obj):
    return isinstance(obj, Endpoint)


@register.filter()
def is_method_field(obj):
    return obj['type'] == 'SerializerMethodField'


@register.filter()
def add_one(value):
    data = value + 1
    return data
