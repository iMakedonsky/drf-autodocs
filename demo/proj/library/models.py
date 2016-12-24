import uuid

from django.db import models


class Library(models.Model):
    THEME_CHOICES = (
        ('scientific', 'Scientific'),
        ('home', 'Home'),
        ("children's", "Children's")
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=THEME_CHOICES)


class Book(models.Model):
    author = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    uuid = models.UUIDField(default=uuid.uuid4)
    library = models.ForeignKey(Library, related_name='books')
