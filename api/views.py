from django.shortcuts import render
from . import models 
from . import serializers 
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework import status



class CartView(APIView):


    def get(self, request):
        objects = models.Cart.objects.all()
        serializer = serializers.CartSerialzer(objects, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = serializers.CartSerialzer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CartUpdateView(APIView):
    def patch(self, request, pk):
        objects = models.Cart.objects.filter(pk=pk).first()
        serializer = serializers.CartSerialzer(objects, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        models.Cart.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_200_OK)





class CategoryView(APIView):


    def get(self, request):
        objects = models.Category.objects.all()
        serializer = serializers.CategorySerialzer(objects, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = serializers.CategorySerialzer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoryUpdateView(APIView):
    def patch(self, request, pk):
        objects = models.Category.objects.filter(pk=pk).first()
        serializer = serializers.CategorySerialzer(objects, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        models.Category.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_200_OK)





