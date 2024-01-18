from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# Create your views here.
class HomeAPIView(APIView):
    def get(self, request):
        data = {'message':"this is test!"}
        return Response(data, status=status.HTTP_200_OK)

class PageAPIView(APIView):
    def get(self, request, format=None):
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        name = request.data.get('name', None)

        if name is not None:
            new_page = Page(name=name)
            new_page.save()

            serializer = PageSerializer(new_page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': 'Name field is required.'}, status=status.HTTP_400_BAD_REQUEST)

