from dataclasses import field
from email.policy import default
from rest_framework import serializers
from .models import *

class CellsSerializer(serializers.ModelSerializer):
  # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = Cells
    depth = 1
    fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
  # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = Tags
    depth = 1
    fields = '__all__'

class MySerializer(serializers.Serializer):
  # content = serializers.CharField()
  time_create = serializers.DateTimeField(read_only=True)
  time_update = serializers.DateTimeField(read_only=True)

class UserSerializer(serializers.ModelSerializer):
    print('test Userserlerl')

    class Meta:
        model = User
        fields = '__all__'

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user