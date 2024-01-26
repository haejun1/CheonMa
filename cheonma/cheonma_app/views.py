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
    def get(self, request):
        pages = Page.objects.all()
        pages_serializer = PageSerializer(pages, many=True).data
        return Response(pages_serializer, status=status.HTTP_200_OK)
    0
    def post(self, request):
        name = request.data.get('name', None)

        if name is not None:
            new_page = Page(name=name)
            new_page.save()

            serializer = PageSerializer(new_page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': 'Name field is required.'}, status=status.HTTP_400_BAD_REQUEST)

class LevelAPIView(APIView):
    def post(self, request):
        page_id = request.data.get('page', None)

        # Check if the page already has level 8
        if Level.objects.filter(page=page_id, level=8).exists():
            return Response({'error': '이미 모든 비급을 제작하였습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        # Find the current highest level for the given page
        current_highest_level = Level.objects.filter(page=page_id).order_by('-level').first()

        # Determine the next level to be posted
        next_level = current_highest_level.level + 1 if current_highest_level else 1

        # Create a new Level instance and set effect and level
        new_level = Level(page_id=page_id, level=next_level)
        new_level.set_effect_and_level(page=page_id)
        new_level.set_state()

        serializer = LevelSerializer(new_level)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
