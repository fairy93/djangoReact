from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from icecream import ic

User = get_user_model()


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if User.objects.filter(email=email).exists():
            item = User.objects.get(email=email)

            if check_password(password, item.password):
                if user is None:
                    return {
                        'email': 'None'
                    }
                try:
                    payload = JWT_PAYLOAD_HANDLER(user)
                    jwt_token = JWT_ENCODE_HANDLER(payload)
                    update_last_login(None, user)
                except User.DoesNotExist:
                    raise serializers.ValidationError(
                        'User with given email and password does not exists'
                    )
                return {
                    'email': user.email,
                    'token': jwt_token
                }
            return HttpResponse(status=401)
