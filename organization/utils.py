from tenant_schemas.utils import schema_exists
from .models import Organization
import os

def has_schema_name(schema):
    return Organization.objects.filter(schema_name = schema).exists()

def generate_unique_schema_name(input_str):
    schema_name = input_str.lower() if len(input_str) == 1 else ''.join([word[0].lower() for word in input_str.split()])
    while has_schema_name(schema_name):
      schema_name = ''.join([word[:2].lower() for word in input_str.split()])
      input_str = input_str.replace(" ", "  ")  # Replace single spaces with double spaces  
    return schema_name


def get_domain(schema_name):
    domain = os.environ.get("BASE_DOMAIN")
    domain_url = '.'.join([schema_name,domain])
    return domain_url