from rest_framework import serializers
from library.models import Library, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ('uuid',)
        fields = '__all__'
        model = Book


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'author')
        model = Book

    def to_representation(self, instance):
        return LibrarySerializer(instance.library)


class LibrarySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Library
