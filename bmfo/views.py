from os import stat
import re
from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer
from rest_framework import status
from django.contrib.auth import authenticate
import jwt
from django.conf import settings
from .models import CustomUser, Product
import json

@api_view(['POST'])
def join(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    print(request.data)
    nickname = request.data["nickname"]
    password = request.data["password"]
    if not nickname or not password:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(nickname=nickname, password=password)
    if user is not None:
        encode_jwt = jwt.encode({"id": user.pk}, settings.SECRET_KEY, algorithm="HS256")
        response = Response()
        response.data = {"token": encode_jwt}
        return response
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])  
def userview(request):
    token = request.GET['token']
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    user = CustomUser.objects.get(id=payload['id'])
    serializer = UserSerializer(user)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request):
    print(request.GET)
    category = request.GET.get('category')
    products = Product.objects.filter(category=category)
    items = []
    for i in products:
        serializer = ProductSerializer(i)
        items.append(serializer.data)
    return Response(data = items)


@api_view(['POST'])
def addProduct(request):
    product = ProductSerializer(data = request.data)
    if product.is_valid() :
        product.save()
    return Response(status=status.HTTP_200_OK)
