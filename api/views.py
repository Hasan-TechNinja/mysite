from django.shortcuts import render, get_object_or_404
from todo.models import Database
from rest_framework.views import APIView, Response, status
from . serializers import DatabaseSerializers
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def fetchData(request):
    if request.method == "GET":
        data = Database.objects.all()
        serializer = DatabaseSerializers(data, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
         serializer = DatabaseSerializers(data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
             return Response(serializer.errors)
         

class TodoAPI(APIView):
    def get(self, request):
        data = Database.objects.all()
        serializer = DatabaseSerializers(data, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DatabaseSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    

class TodoAPIDetails(APIView):
    def get(self, request, pk):
        data = Database.objects.get(id = pk)
        serializer = DatabaseSerializers(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        data = Database.objects.get(id= pk)
        serializer = DatabaseSerializers(data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
        
    def delete(self, request, pk):
        data = Database.objects.get(pk = pk)
        data.delete()
        return Response(status=status.HTTP_200_OK)