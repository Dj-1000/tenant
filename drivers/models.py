from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
