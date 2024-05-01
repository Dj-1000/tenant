from rest_framework import serializers
from .models import Shipment
from drivers.serializers import DriverSerializer
from locations.serializers import LocationSerializer
from locations.models import Location
from drivers.models import Driver
from rest_framework.exceptions import ValidationError

class ShipmentSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()
    origin = LocationSerializer()
    destination = LocationSerializer()
    class Meta:
        model = Shipment
        fields = ('id','driver','origin','destination')
        
    def validate(self, validated_data):
        payload = validated_data
        origin_id = payload.get("origin")
        destination_id = payload.get("destination")
        driver_id = payload.get("driver")
        if not Driver.objects.filter(id = driver_id).exists():
            raise ValidationError({"driver" : "invalid driver id"})
        
        if not Location.objects.filter(id = origin_id).exists():
            raise ValidationError({'origin': 'invalid origin address'})
        
        if not Location.objects.filter(id = destination_id).exists():
            raise ValidationError({'destination': 'invalid destination address'})
        
        return validated_data 
        
    