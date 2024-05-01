from django.db import models
from tenant_schemas.models import TenantMixin

class Organization(TenantMixin):
    name = models.CharField(max_length=100)    
    def __str__(self) -> str:
        return self.name
