from dataclasses import field
from email.policy import default
from rest_framework import serializers
from .models import *

class CellsSerializer(serializers.ModelSerializer):
  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = Cells
    depth = 1
    fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = Tags
    depth = 1
    fields = '__all__'

class MySerializer(serializers.Serializer):
  # content = serializers.CharField()
  time_create = serializers.DateTimeField(read_only=True)
  time_update = serializers.DateTimeField(read_only=True)

