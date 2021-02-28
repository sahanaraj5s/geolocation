from .views import GeolocationCreateViews
from django.urls import path

urlpatterns = [
    path('create/', GeolocationCreateViews.as_view(), name='location')
]
