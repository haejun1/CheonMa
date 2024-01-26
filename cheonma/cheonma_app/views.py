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

        smallest_null_state_level = Level.objects.filter(page=page_id, state__isnull=True).order_by('level').first()

        if smallest_null_state_level:
            smallest_null_state_level.set_state()
            smallest_null_state_level.save()
            serializer = LevelSerializer(smallest_null_state_level)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': '모든 비급이 제작 완료되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)

class LockAPIView(APIView):
    def post(self, request):
        page_id = request.data.get('page', None)
        level_number = request.data.get('level', None)

        if page_id is None or level_number is None:
            return Response({'error': 'Both "page" and "level" are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            page_id = int(page_id)
            level_number = int(level_number)
        except ValueError:
            return Response({'error': 'Invalid page or level format.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            level = Level.objects.get(page_id=page_id, level=level_number)
        except Level.DoesNotExist:
            return Response({'error': 'Specified page or level does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        level.lock = not level.lock
        level.save()

        return Response({'message': '잠금상태가 업데이트 됐습니다.'}, status=status.HTTP_200_OK)

class ResetAPIView(APIView):
    def post(self, request):
        page_id = request.data.get('page', None)

        if page_id is None:
            return Response({'error': '맞는 페이지가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            page_id = int(page_id)
        except ValueError:
            return Response({'error': 'Invalid page format.'}, status=status.HTTP_400_BAD_REQUEST)

        levels_to_reset = Level.objects.filter(page_id=page_id)

        for level in levels_to_reset:
            if not level.lock:
                level.state = None
                level.save()

        return Response({'message': f'Level information for page {page_id} reset successfully.'}, status=status.HTTP_200_OK)