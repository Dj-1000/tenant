from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DriverSerializer
from rest_framework.exceptions import ValidationError
from.models import Driver

class ListDriver(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    
    
class DriverView(APIView):
    def get(self,request,pk):
        obj = Driver.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"driver":"driver does not exist"})

        seri = DriverSerializer(obj)
        return Response({
            "status" : status.HTTP_200_OK,
            "result" : seri.data
        })
        
    def post(self,request):
        seri = DriverSerializer(data = request.data)
        if seri.is_valid():
            seri.save()
            return Response({
                "status" : status.HTTP_201_CREATED,
                "result_message" : "Driver has been successfully registered"
            })
        else:
            return Response({
                "status" : status.HTTP_400_BAD_REQUEST,
                "result_message" : seri.errors
            })
            
    def put(self,request,pk):
        obj = Driver.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"driver":"driver does not exist"})
        
        seri = DriverSerializer(obj,data = request.data)
        if seri.is_valid():
            seri.save()
            return Response({
                "status" : status.HTTP_200_OK,
                "result_message" : "Driver has been successfully updated"
            })
        else:
            return Response({
                "status" : status.HTTP_400_BAD_REQUEST,
                "result_message" : seri.errors
            })
            
    def delete(self,request,pk):
        obj = Driver.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"driver":"driver does not exist"})
        
        obj.delete()
        return Response({
            "status" : status.HTTP_200_OK,
            "result_message" : "Driver has been successfully deleted"
        })
    


