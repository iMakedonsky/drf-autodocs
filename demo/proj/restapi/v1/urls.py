from django.conf.urls import url, include
from .library import views as library_views
from .university import views as university_views


library_urlpatterns = [
    url(r'^books$', library_views.BooksHandler.as_view(), name='books'),
    url(r'^books/(?P<pk>\d+)/$', library_views.BookReadUpdateHandler.as_view(), name='book_read_update'),
    url(r'^libraries/$', library_views.LibrariesHandler.as_view(), name='libraries'),
]

university_urlpatterns = [
    url(r'^lecturers/$', university_views.LecturersHandler.as_view(), name='lecturers'),
    url(r'^lecturers/(?P<pk>\d+)/$', university_views.LecturerUpdateHandler.as_view(), name='lecturer_read_update'),
    url(r'^universities/$', university_views.UniversitiesHandler.as_view(), name='universities'),
]

urlpatterns = [
    url(r'^library/', include(library_urlpatterns, namespace='library')),
    url(r'^university/', include(university_urlpatterns, namespace='university')),
]
