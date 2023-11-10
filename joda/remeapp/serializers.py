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
    exclude = ['users']

class TagsSerializer(serializers.ModelSerializer):
  # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = Tags
    depth = 1
    fields = '__all__'
    exclude = ['users']

class UserSer(serializers.ModelSerializer):
    print('test Userserlerl')
    class Meta:
        model = User
        exclude = ['password']
        
        # fields = '__all__'
