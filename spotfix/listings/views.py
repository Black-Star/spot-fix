from rest_framework import generics

# Create your views here.
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication

from listings.serializers import SpotFixSerializer
from listings.models import SpotFix


@authentication_classes((TokenAuthentication,))
class SpotFixList(generics.RetrieveAPIView):
    queryset = SpotFix.objects.all()
    serializer_class = SpotFixSerializer
