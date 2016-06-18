from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter

from listings.serializers import SpotFixSerializer
from listings.models import SpotFix
from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 12


class SpotFixList(viewsets.ReadOnlyModelViewSet):
    queryset = SpotFix.objects.all()
    serializer_class = SpotFixSerializer
    distance_filter_field = 'point'
    pagination_class = StandardResultsSetPagination
    filter_backends = (DistanceToPointFilter, )
    bbox_filter_include_overlapping = True


# @authentication_classes((TokenAuthentication,))
class LocationList(viewsets.ModelViewSet):
    queryset = SpotFix.objects.all()
    serializer_class = SpotFixSerializer
    distance_filter_field = 'point'
    pagination_class = StandardResultsSetPagination
    filter_backends = (DistanceToPointFilter, )
    bbox_filter_include_overlapping = True
