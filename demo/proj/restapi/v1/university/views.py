from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from university.models import University, Lecturer
from .serializers import (
    LecturerSerializer,
    UniversitySerializer
)


class UniversitiesHandler(ListCreateAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()


class LecturerUpdateHandler(RetrieveUpdateAPIView):
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()


class LecturersHandler(ListCreateAPIView):
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()


