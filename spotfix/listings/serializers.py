from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from listings.models import (SpotFix, Location)


class SpotFixSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SpotFix
        # fields = ('id', 'owner', 'current_status')


class LocationSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = Location
        geo_field = "point"

        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'address', 'city', 'state')
