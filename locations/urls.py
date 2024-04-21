from django.urls import path

from .views import LocationListCreateAPIView


urlpatterns = [
    path("", LocationListCreateAPIView.as_view())
]
