from django.urls import path
from .views import ListShipment,ShipmentView
urlpatterns = [
    path("add-shipment/",ShipmentView.as_view()),
    path("list/",ListShipment.as_view()),
    path("list/<int:pk>",ShipmentView.as_view()),
    path("update-shipment/<int:pk>",ShipmentView.as_view()),
    path("delete-shipment/<int:pk>",ShipmentView.as_view()),
]