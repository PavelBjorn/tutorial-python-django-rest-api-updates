from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework_jwt.settings import api_settings
from .utils import get_expires

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_respose_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class UserRegisterSerailizer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    token_response = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            'token_response'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_expires(self, obj):
        return get_expires()

    def get_token_response(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        respones = jwt_respose_payload_handler(token, user)
        return respones

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this email already exists")
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this name already exists")
        return value

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')
        print(data)
        if pw != pw2:
            raise serializers.ValidationError("Passwords mast match!")
        return data

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
        )
        user.set_password(raw_password=validated_data.get('password'))
        user.save()
        return user
