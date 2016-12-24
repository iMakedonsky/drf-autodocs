from django.db import models

from library.models import Library


class University(models.Model):
    name = models.CharField(max_length=50)
    libraries = models.ManyToManyField(Library, related_name='libraries')


class Lecturer(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, related_name='lecturers')

