from rest_framework import serializers
from django.contrib.auth import get_user_model
from status.api.serializers import StatusInlineUserSerializer
from rest_framework.reverse import reverse as api_reverse

User = get_user_model()


# django_hosts?

class UserDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    # To sew how to work with
    # statuses = serializers.HyperlinkedRelatedField(
    #     source='status_set',  # Status.objects.filter(user=user)
    #     many=True,
    #     read_only=True,
    #     lookup_field='id',
    #     view_name='api-status:detail'
    # )

    # statuses = StatusInlineUserSerializer(source='status_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'url',
            'status',
            'statuses'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return api_reverse("api-user:detail", kwargs={"username": obj.username}, request=request)

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
            'last': StatusInlineUserSerializer(qs.first(), context={'request': request}).data,
            'recent': StatusInlineUserSerializer(qs[:limit], many=True, context={'request': request}).data
        }
