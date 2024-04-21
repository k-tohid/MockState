from rest_framework import generics

from .models import Location
from .serializers import LocationSerializer


class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
