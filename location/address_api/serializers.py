from location.models import Geolocation
from rest_framework import serializers
from geopy.geocoders import GoogleV3
import re
from django.contrib.auth import settings


class GeolocationSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField("location")
    address = serializers.CharField(max_length=256, required=True)
    output_format = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = Geolocation
        fields = ('coordinates', 'address', 'output_format')

    def location(self, obj):
        geolocator = GoogleV3(api_key=settings.API_KEY)
        address = re.sub("[^a-zA-Z0-9 \n\.]", '', obj.address)
        # address = address.replace('#', '')
        google_response = geolocator.geocode(address)
        latitude = google_response[1][0]
        longitude = google_response[1][1]
        return {"lat": latitude, "log": longitude}
