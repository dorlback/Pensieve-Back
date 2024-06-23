from rest_framework import serializers
from .models import Tag, Note, NoteUser
from user.serializer import UserSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.urls import reverse

class TagSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['pk', 'user', 'title', 'created_date', 'links']
        read_only_fields = ['pk', 'created_date']

    def get_links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self-list-create",
                "href": request.build_absolute_uri(reverse('tag-list-create'))
            },
            {
                "rel": "self-detail-update-destroy",
                "href": request.build_absolute_uri(reverse('tag-detail-update-destroy', args=[obj.pk]))
            }
        ]

class NoteSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['pk', 'title', 'content', 'tags', 'created_date', 'links']
        read_only_fields = ['pk', 'created_date']

    def get_tags(self, obj):
        tags = Tag.objects.filter(note=obj)
        return TagSerializer(tags, many=True).data

    def get_links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self-list-create",
                "href": request.build_absolute_uri(reverse('note-list-create'))
            },
            {
                "rel": "self-detail-update-destroy",
                "href": request.build_absolute_uri(reverse('note-detail-update-destroy', args=[obj.pk]))
            },
            {
                "rel": "tag-list-create",
                "href": request.build_absolute_uri(reverse('tag-list-create'))
            },
        ]

class NoteUserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = UserSerializer()
    note = NoteSerializer()
    links = serializers.SerializerMethodField()

    class Meta:
        model = NoteUser
        fields = ['pk', 'user', 'note', 'role', 'created_date']
        read_only_fields = ['pk', 'created_date']

    def get_links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self-list-create",
                "href": request.build_absolute_uri(reverse('noteuser-list-create'))
            },
            {
                "rel": "self-detail-update-destroy",
                "href": request.build_absolute_uri(reverse('noteuser-detail-update-destroy', args=[obj.pk]))
            },
        ]