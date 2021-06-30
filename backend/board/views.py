from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from board.serializers import boardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from icecream import ic


class Posts(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = boardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)


class Post(APIView):
    def get(self, request):
        pass


# class Auth(APIView):
#     def get(self, request):
#         # ic(request)
#         ic('저장1')
#         serializer = MemberSerializer(data=request)
#         if serializer.is_valid():
#             ic('저장2ㄴ')
#             serializer.sae()
#         return Response({'result': 'WELCOME'})

@csrf_exempt
def post_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        snippets = Post.objects.all()
        serializer = boardSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = boardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
