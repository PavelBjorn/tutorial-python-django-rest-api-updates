from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerailizer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        qs = User.objects.filter(email__ixact=value)
        if qs.exist():
            raise serializers.ValidationError("User with this email already exists")
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username_iexact=value)
        if qs.exist():
            raise serializers.ValidationError("User with this name already exists")

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Passwords mast match!")
        return data

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
        )
        user.set_password(raw_password=validated_data.get('password'))
        user.save()
        return user
