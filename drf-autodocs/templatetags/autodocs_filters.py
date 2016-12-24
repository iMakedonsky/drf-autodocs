from rest_framework.utils.formatting import markup_description
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeData
from django.utils.text import normalize_newlines
from django.utils.html import escape


register = template.Library()


@register.filter(name='markdown')
@stringfilter
def markdown(value):
    return markup_description(value)


@register.filter(name='is_dict')
def is_dict(obj):
    return isinstance(obj, dict)


@register.filter(is_safe=True, needs_autoescape=True, name='keep_formatting')
@stringfilter
def keep_spacing(value, autoescape=None):
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    value = mark_safe(value.replace('  ', ' &nbsp;').replace('\t', '&emsp;'))
    return mark_safe(value.replace('\n', '<br />'))
