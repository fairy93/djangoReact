from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from icecream import ic
from member.serializers import MemberSerializer, UserLoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    ic(request)
    serializer = MemberSerializer(data=request.data['body'])
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data['body'])
        if not serializer.is_valid():
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['username'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)
        response = {
            'success': True,
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)
