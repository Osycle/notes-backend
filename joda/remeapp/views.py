import json
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated



# IsAuthenticatedOrReadOnly - только автаризованные
# IsAdminUser - только автаризованные

# class CellsAPIView(generics.ListAPIView):
#   queryset = Cells.objects.all()
#   serializer_class = CellsSerializer

class CellsViewSet(viewsets.ModelViewSet):
  serializer_class = CellsSerializer
  permission_classes = (IsAuthenticated,)
  queryset = Cells.objects.all()
  def list(self, request):
    cells_all = Cells.objects.all()
    tags_all = Tags.objects.all()
    print('METHOD LIST')
    return Response({
      "cells": CellsSerializer(cells_all, many=True).data,
      "tags": TagsSerializer(tags_all, many=True).data,
    })

  def create(self, request):
    data = request.data
    cell_new = Cells.objects.create(content=data['content'], user_id=request.user.id)
    if 'tags' in data:
      cell_new.set_cell_tags(data['tags'], request.user.id)
    return Response({
      "status": True,
      "cell": CellsSerializer(cell_new).data
    })

  def edit(request, pk=None):
    data = request.data
    update_tags = data['tags']
    print(request.data, request, 'request.data', pk, 'pk')
    try:
      cell = Cells.objects.get(pk=pk)
    except:
      return Response({"error": "Object does not exists"})
    # print(request.user.id, 'request.user.id', pk, 'pk')
    for tag in cell.tags.all():
      if not tag.name in update_tags:
        if not Cells.objects.exclude(pk=pk).filter(tags__name=tag.name):
          Tags.objects.get(pk=tag.pk).delete()
    cell.set_cell_tags(update_tags, request.user.id)
    cell_ser = CellsSerializer(data=data, instance=cell)          
    cell_ser.is_valid(raise_exception=True)
    cell_ser.save(commit=False)
    print(cell_ser, 'cell_ser')
    return Response({
      "status": True,
      "cell": cell_ser.data
    })

  def delete(request, pk=None):
    cell = Cells.objects.get(pk=pk)
    for tag in cell.tags.all():
      if not Cells.objects.exclude(pk=pk).filter(tags__name=tag.name):
        Tags.objects.get(pk=tag.pk).delete()
    cell_id = cell.id
    result = cell.delete()
    return Response({
      "status": True,
      "cell_id": cell_id,
      "result": result
    })

class TagsViewSet(viewsets.ModelViewSet):
  serializer_class = TagsSerializer
  permission_classes = (IsAuthenticated,)
  # permission_classes = (IsOwnerOrReadOnly,)
  def list(self, request):
    tags_all = Tags.objects.all()
    return Response({
      "status": True,
      "tags": TagsSerializer(tags_all, many=True).data,
    })

class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSer
  # permission_classes = (IsOwnerOrReadOnly,)
  # queryset = User.objects.all()
  def list(self, request):
    print(request.user.id)
    tags_all = User.objects.filter(pk=request.user.id)
    # print(list(tags_all), 'pint2')
    return Response({
      "tags": UserSer(tags_all, many=True).data,
    })
