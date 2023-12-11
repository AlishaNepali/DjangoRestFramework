from itertools import product
from turtle import st
from urllib import request, response
from django.shortcuts import render
from home.models import Product
from home.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ProductAPIView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
# class ProductDetailAPIView(APIView):
#     def get_objects(slef, id):
#         try:
#             return Product.objects.get(id=id)
#         except Product.DoesNotExist:
#             return response(status-status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         product = self.get_objects(id)
#         serializer = ProductSerializer(product)
#         return response(serializer.data)

    

#     def put(self,request,id):
#         product = self.get_objects(id)
#         serializer = ProductSerializer(product, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response(serializer.data, status=status.HTTP_201_CREATED)
#         return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)