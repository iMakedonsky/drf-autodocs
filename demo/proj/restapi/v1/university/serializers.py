from university.models import University, Lecturer
from rest_framework import serializers


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = University


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Lecturer



