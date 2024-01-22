from rest_framework import serializers
from .models import *

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['page', 'level', 'effect', 'lock', 'state']
        
class PageSerializer(serializers.ModelSerializer):
    levels = LevelSerializer(many=True, read_only=True)
    class Meta:
        model = Page
        fields = ['id', 'name', 'levels']
