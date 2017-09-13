# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from appone.serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def getBaseAssets():
    try:
        groupList = Group.objects.all()
    except:
        groupList = []
    return {"group":groupList}


def assets_config(request):
    return render_to_response('assets_config.html',{"user":request.user,"baseAssets":getBaseAssets()})


@api_view(['GET', 'POST' ])
def group_list(request,format=None):
    if request.method == 'GET':
        snippets = Group.objects.all()
        serializer = GroupSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # if not  request.user.has_perm('Opsmanage.change_group'):
        #     return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
