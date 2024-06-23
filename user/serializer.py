from rest_framework import serializers
from .models import User
from django.urls import reverse

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['pk', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'links']
        read_only_fields = ['pk', 'date_joined']

    def get_links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self-list-create",
                "href": request.build_absolute_uri(reverse('user-list-create'))
            },
            {
                "rel": "self-detail-update-destroy",
                "href": request.build_absolute_uri(reverse('user-detail-update-destroy', args=[obj.email]))
            },
        ]