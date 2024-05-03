from django.db import models
from locations.models import Location
from drivers.models import Driver

class Shipment(models.Model):
    origin = models.ForeignKey(Location, on_delete=models.CASCADE,related_name='origin_loc')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE,related_name='destination_loc')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,related_name='shipment')
    completion = models.DateTimeField(auto_now=True)
