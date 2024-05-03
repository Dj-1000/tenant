from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("org/",include("organization.urls")),
    path("driver/",include("drivers.urls")),
    path("location/",include("locations.urls")),
    path("shipment/",include("shipments.urls")),
]
