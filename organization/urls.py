from django.urls import path
from .views import ListOrganization, OrganizationView
urlpatterns = [
    path('add-org/', OrganizationView.as_view()),
    path('list/', ListOrganization.as_view()),
    path('list/<int:pk>',OrganizationView.as_view()),
]