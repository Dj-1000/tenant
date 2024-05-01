from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LocationSerializer
from rest_framework.exceptions import ValidationError
from.models import Location

class ListLocations(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
    
class LocationView(APIView):
    def get(self,request,pk):
        obj = Location.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"driver":"driver does not exist"})

        seri = LocationSerializer(obj)
        return Response({
            "status" : status.HTTP_200_OK,
            "result" : seri.data
        })
        
    def post(self,request):
        seri = LocationSerializer(data = request.data)
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
        obj = Location.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"driver":"driver does not exist"})
        
        seri = LocationSerializer(obj,data = request.data)
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
        obj = Location.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"driver":"driver does not exist"})
        
        obj.delete()
        return Response({
            "status" : status.HTTP_200_OK,
            "result_message" : "Driver has been successfully deleted"
        })
    


