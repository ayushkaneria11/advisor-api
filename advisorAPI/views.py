from django.shortcuts import render
from .models import Advisor
from rest_framework import serializers
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes 
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
# Create your views here.

@api_view(['POST',])
@permission_classes([AllowAny])
def addAdvisor(request):
    serializers = AddAdvisorSerializer(data=request.data,many=False)
    # HttpResponse(request.data)
    if serializers.is_valid():
        serializers.addAdvisor()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
@permission_classes([AllowAny])
def registerUser(request):
    serializers = registerUserSerializer(data=request.data,many=False)
    if serializers.is_valid():
        user = serializers.registerUser()
        return Response(data={"user_id":user.id},status=status.HTTP_200_OK)
    else:
        return Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def loginUser(request):
    serializers = loginUserSerializer(data=request.data,many=False)
    if serializers.is_valid():
        user = serializers.loginUser()
        return Response(data={'user_id':user.id,'username':user.username},status=status.HTTP_200_OK)
    else:
        return Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)

