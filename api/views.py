from django.shortcuts import render
from todo.models import Database
from rest_framework.views import APIView, Response, status
from . serializers import DatabaseSerializers
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def fetchData(request):
    if request.method == "GET":
        data = Database.objects.all()
        serializer = DatabaseSerializers(data, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
         return Response(serializer.errors)