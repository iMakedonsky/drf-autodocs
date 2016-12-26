from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from university.models import University, Lecturer
from .serializers import (
    LecturerSerializer,
    UniversitySerializer
)


class UniversitiesHandler(ListCreateAPIView):
    """
    Shiny and nice docstring, which:
        1) allows formatting
        2) `allows markdown`
    """
    serializer_class = UniversitySerializer
    queryset = University.objects.all()


class LecturerUpdateHandler(RetrieveUpdateAPIView):
    """
    Shiny and nice docstring, which:
        1) allows formatting
        2) `allows markdown`
    """
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()


class LecturersHandler(ListCreateAPIView):
    """
    Shiny and nice docstring, which:
        1) allows formatting
        2) `allows markdown`
    """
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()


