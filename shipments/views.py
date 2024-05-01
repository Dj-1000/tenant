from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ShipmentSerializer
from rest_framework.exceptions import ValidationError
from.models import Shipment
from django.forms import model_to_dict

class ListShipment(generics.ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    
    
class ShipmentView(APIView):
    def get(self,request,pk):
        obj = Shipment.objects.filter(id = pk).first()
        ## may require to add model_to_dict here
        ## dict_obj = model_to_dict(obj)
        if not obj:
            raise ValidationError({"shipment":"shipment does not exist"})

        seri = ShipmentSerializer(obj)
        return Response({
            "status" : status.HTTP_200_OK,
            "result" : seri.data
        })
        
    def post(self,request):
        
        seri = ShipmentSerializer(data = request.data)
        if seri.is_valid():
            seri.save()
            return Response({
                "status" : status.HTTP_201_CREATED,
                "result_message" : "Shipment has been successfully registered"
            })
        else:
            return Response({
                "status" : status.HTTP_400_BAD_REQUEST,
                "result_message" : seri.errors
            })
            
    def put(self,request,pk):
        obj = Shipment.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"shipment":"shipment does not exist"})
        
        seri = ShipmentSerializer(obj,data = request.data)
        if seri.is_valid():
            seri.save()
            return Response({
                "status" : status.HTTP_200_OK,
                "result_message" : "Shipment has been successfully updated"
            })
        else:
            return Response({
                "status" : status.HTTP_400_BAD_REQUEST,
                "result_message" : seri.errors
            })
            
    def delete(self,request,pk):
        obj = Shipment.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"shipment":"shipment does not exist"})
        
        obj.delete()
        return Response({
            "status" : status.HTTP_200_OK,
            "result_message" : "Shipment has been successfully deleted"
        })
    


