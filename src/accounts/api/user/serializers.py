from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    status_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'url',
            'status_list'
        ]

    def get_url(self, obj):
        return "/api/users/{name}/".format(name=obj.username)

    def get_status_list(self, obj):
        return "Not implemented yet" #TODO
