from rest_framework import serializers
from .models import Book, Author
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.urls import reverse

# 작가 시리얼라이저
class AuthorSrializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['pk', 'name', 'links', 'books']
        read_only_fields = ['pk']

    def get_books(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "related-books",
                "href": request.build_absolute_uri(reverse('book-detail-update-destroy', args=[book.pk]))
            } for book in obj.author_id.all()
        ]

    def get_links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self-list-create",
                "href": request.build_absolute_uri(reverse('author-list-create'))
            },
            {
                "rel": "self-detail-update-destroy",
                "href": request.build_absolute_uri(reverse('author-detail-update-destroy', args=[obj.pk]))
            }
        ]

# 책 시리얼라이저
class BookSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    author = AuthorSrializer()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'price', 'created_date', 'links']
        read_only_fields = ['pk', 'created_date']
        extra_kwargs = {
            'price': {'required': False},
        }

    def get_links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self-list-create",
                "href": request.build_absolute_uri(reverse('book-list-create'))
            },
            {
                "rel": "self-detail-update-destroy",
                "href": request.build_absolute_uri(reverse('book-detail-update-destroy', args=[obj.pk]))
            },
            {
                "rel": "author-list-create",
                "href": request.build_absolute_uri(reverse('author-list-create'))
            },
            {
                "rel": "author-detail-update-destroy",
                "href": request.build_absolute_uri(reverse('author-detail-update-destroy', args=[obj.author.pk]))
            }
        ]