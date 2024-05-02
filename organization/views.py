from rest_framework.views import APIView
from .models import Organization
from rest_framework.generics import ListAPIView
from .serializers import OrgSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .utils import generate_unique_schema_name, get_domain

class ListOrganization(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer
    
class OrganizationView(APIView):
    def get(self,request,pk):
        obj = Organization.objects.filter(id = pk).first()
        if not obj:
            raise ValidationError({"organization":"organization does not exist"})

        #dict_obj = model_to_dict(obj)
        seri = OrgSerializer(obj)
        return Response({
            "status" : status.HTTP_200_OK,
            "result" : seri.data
        })
        
    def post(self, request):
        payload = request.data
        name = payload.get("org_name")
        schema = generate_unique_schema_name(name)
        domain_url = get_domain(schema_name=schema)
        if not name:
            raise ValidationError({"org_name":"organization name is required"})
        
        org = Organization.objects.create(
            domain_url = domain_url,
            schema_name = schema,
            org_name = name
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        