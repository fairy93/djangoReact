
import json
from .models import membervo
from rest_framework.views import APIView
from rest_framework.response import Response
from member.serializers import MemberSerializer
from icecream import ic
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from member.serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic
from rest_framework.parsers import JSONParser

class Members(APIView):
    def post(self, request):
        # data = request.data['body']
        data = json.loads(request.body)
        membervo.objects.create()
        ic(data)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)


class Member(APIView):
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
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        snippets = Member.objects.all()
        serializer = MemberSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
