from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HomeAPIView(APIView):
    def get(self, request):
        data = {'message':"this is test!"}
        return Response(data, status=status.HTTP_200_OK)