from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from member.serializers import UserCreateSerializer, UserLoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])  # 인증 필요없다
def signup(request):
    ic('입장')
    ic(request.data)
    serializer = UserCreateSerializer(data=request.data['body'])
    if serializer.is_valid(raise_exception=True):
        serializer.save()  # DB 저장
        return Response(serializer.data, status=201)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data['body'])
        ic(serializer)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":  # email required
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)
        response = {
            'success': True,
            'token': serializer.data['token']  # 시리얼라이저에서 받은 토큰 전달
        }
        ic(Response)
        return Response(response, status=status.HTTP_200_OK)
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from icecream import ic
# from member.serializers import MemberSerializer, UserLoginSerializer
#
#
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def signup(request):
#     ic(request)
#     ic(request.data)
#     serializer = MemberSerializer(data=request.data['body'])
#     if serializer.is_valid():
#         serializer.save()
#         ic(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=400)
#
#
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     if request.method == 'POST':
#         ic('실행')
#         serializer = UserLoginSerializer(data=request.data['body'])
#         if not serializer.is_valid():
#             return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
#         if serializer.validated_data['username'] == "None":
#             return Response({'message': 'fail'}, status=status.HTTP_200_OK)
#         response = {
#             'success': True,
#             'token': serializer.data['token']
#         }
#         return Response(response, status=status.HTTP_200_OK)
