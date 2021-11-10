from rest_framework import serializers

from status.models import Status
from accounts.api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse


class StatusSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    # To see how to do it
    # user_link = serializers.HyperlinkedRelatedField(
    #     source='user',  # user foreign key
    #     lookup_field='username',
    #     view_name='api-user:detail',
    #     read_only=True
    # )

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            # 'user_link',
            'content',
            'image',
            'url'
        ]
        read_only_fields = ['user']

    def get_user(self, obj):
        request = self.context.get('request')
        user = obj.user
        return UserPublicSerializer(user, read_only=True, context={"request": request}).data

    def get_url(self, obj):
        request = self.context.get('request')
        return api_reverse('api-status:detail', kwargs={"id": obj.id}, request=request)

    def validate_content(self, value):
        if len(value) > 1000000:
            raise serializers.ValidationError("This is wayy too long")
        return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Status should have content or image")
        return data


class StatusInlineUserSerializer(StatusSerializer):
    class Meta(StatusSerializer.Meta):
        fields = [
            'id',
            'content',
            'image',
            'url'
        ]
