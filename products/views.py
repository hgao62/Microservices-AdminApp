from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, User
from .serializers import ProductSerializer
import random

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #/api/products
        products = Product.objects.all()
        serialzer = ProductSerializer(products, many=True)
        return Response(serialzer.data)
    
    def create(self, request): #/api/products
        serialzer = ProductSerializer(data=request.data)
        serialzer.is_valid(raise_exception =True)
        serialzer.save()
        return Response(serialzer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk = None):
        pass
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(products, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def retrieve(self, request, pk =None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def destroy(self, request, pk =None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({"id":user.id})