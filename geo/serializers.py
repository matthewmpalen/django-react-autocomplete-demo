from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Location
        fields = ('id', 'city', 'state', 'zipcode', 'full_name')
