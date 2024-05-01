from django.contrib import admin
from django.urls import path
from .views import DriverView, ListDriver

urlpatters = [
    path("driver-add/",DriverView.as_view(), name = "add-driver"),
    path("list/",ListDriver.as_view(), name = "list-all"),
    path("list/<int:pk>",DriverView.as_view(), name = "list"),
    path("update-driver/<int:pk>",DriverView.as_view(), name = "update-driver"),
    path("delete-driver/<int:pk>",DriverView.as_view(), name = "delete-driver"),
    
]