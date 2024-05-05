from .models import Organization
import os

dom = os.environ.get("BASE_DOMAIN")
print(dom)

Organization.objects.create(org_name = 'Public',schema_name = 'public',domain_url = dom)
