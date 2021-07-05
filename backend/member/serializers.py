from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from django.http import JsonResponse, HttpResponse
from icecream import ic
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
import hashlib
User = get_user_model()


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    print(email)

    def create(self, validated_data):
        user = User.objects.create(  # User 생성
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
            ic('실행2')

            item = User.objects.get(email=email)
            a=hashlib.sha256(password.encode())
            b=hashlib.sha256(item.password.encode())
            ic(a)
            ic(b)
  
            if hashlib.sha256(password.encode()) == hashlib.sha256(item.password.encode()):
                ic('실행3')
                if user is None:
                    return {
                        'email': 'None'
                    }
                try:
                    payload = JWT_PAYLOAD_HANDLER(user)
                    jwt_token = JWT_ENCODE_HANDLER(payload)  # 토큰 발행
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

    # def validate(self, data):
    #     email = data.get("email", None)
    #     password = data.get("password", None)
    #     user = authenticate(email=email, password=password)
    #     if User.objects.filter(email=email).exists():
    #         account = User.objects.get(email=email)
    #         if account.password == password: return JsonResponse({'message': 'Login SUCCESS'}, status=200)
    #         return HttpResponse(status=401)
    #     ic('벨라이티;')
    #     ic(user)
    #     if user is None:
    #         return {
    #             'email': 'None'
    #         }
    #     try:
    #         payload = JWT_PAYLOAD_HANDLER(user)
    #         jwt_token = JWT_ENCODE_HANDLER(payload)  # 토큰 발행
    #         update_last_login(None, user)
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError(
    #             'User with given email and password does not exists'
    #         )
    #     return {
    #         'email': user.email,
    #         'token': jwt_token
    #     }
# from django.contrib.auth import authenticate
# from rest_framework import serializers
# from rest_framework_jwt.settings import api_settings
# from django.contrib.auth.models import update_last_login
#
#
# from icecream import ic
# from member.models import Member as member
#
# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
#
#
# class MemberSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#     name = serializers.CharField()
#     email = serializers.EmailField()
#
#     class Meta:
#         model = member
#         db_table = 'members'
#         fields = '__all__'
#
#     def create(self, validated_data):
#         return member.objects.create(**validated_data)
#
#
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         username = data.get("username", None)
#         password = data.get("password", None)
#         user = authenticate(username=username, password=password)
#         ic(user)
#         if user is None:
#             return {
#                 'username': 'None'
#             }
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)  # 토큰 발행
#             update_last_login(None, user)
#         except member.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given username and password does not exists'
#             )
#         return {
#             'username': user.username,
#             'token': jwt_token
#         }
