from rest_framework import serializers
from listings.models import SpotFix


class SpotFixSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SpotFix
        # fields = ('id', 'owner', 'current_status')
