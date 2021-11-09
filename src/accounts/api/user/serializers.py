from rest_framework import serializers
from django.contrib.auth import get_user_model
from status.api.serializers import StatusInlineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'url',
            'status',
        ]

    def get_url(self, obj):
        return "/api/user/{name}/".format(name=obj.username)

    def get_status(self, obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_args = request.GET.get('limit')
            try:
                limit = int(limit_args)
            except:
                pass
        qs = obj.status_set.all().order_by("-timestamp")
        return {
            'url': self.get_url(obj) + "status/",
            'last': StatusInlineUserSerializer(qs.first()).data,
            'recent': StatusInlineUserSerializer(qs[:limit], many=True).data
        }
