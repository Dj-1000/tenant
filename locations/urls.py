from django.contrib import admin
from django.urls import path
from .views import ListLocations, LocationView

urlpatters = [
    path("location-add/",LocationView.as_view(),name="location-add"),
    path("list/",ListLocations.as_view(), name = "list-all"),
    path("list/<int:pk>",LocationView.as_view(), name = "list"),
    path("location-update/<int:pk>",LocationView.as_view()),
    path("location-delete/<int:pk>",LocationView.as_view()),  
]