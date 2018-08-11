from rest_framework.generics import ListAPIView

from .models import Location
from .serializers import LocationSerializer


class LocationListAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
