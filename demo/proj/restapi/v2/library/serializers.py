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
    has_books = serializers.SerializerMethodField(help_text='returns Bool')

    class Meta:
        fields = ('books', 'has_books', 'name', 'type')
        model = Library

    def get_has_books(self, instance):
        return bool(instance.books)
