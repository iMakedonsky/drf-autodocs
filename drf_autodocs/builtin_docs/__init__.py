from rest_framework.filters import OrderingFilter, SearchFilter
from util.rendering import render_fields_list

ordering_filter_docstring = """
Orders objects according to value of some field.
For reverse, put '-' before field name.
Example:
    'api/v1/list-of-objects?ordering=-field'
"""

search_filter_docstring = """
Allows to search items via values in some fields
If item has "^username", "=email" fields available via search,
and you do 'api/endpoint?search=email@example.com',
it will return items which email is exactly search string OR username begins with search string

By default, searches will use case-insensitive partial matches.
Options:
 '^' - starts-with search
 '=' - exact match
 '@' - full-text search
 '$' - regex search
"""

filter_backends = {
    OrderingFilter: ordering_filter_docstring,
    SearchFilter: lambda fields: search_filter_docstring + render_fields_list(*fields)
}


