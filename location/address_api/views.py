from .serializers import GeolocationSerializer
from rest_framework import generics
from location.models import Geolocation
from rest_framework.permissions import AllowAny


class GeolocationCreateViews(generics.CreateAPIView):
    serializer_class = GeolocationSerializer
    permission_classes = [AllowAny]

