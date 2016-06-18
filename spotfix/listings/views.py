from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter

from listings.serializers import SpotFixSerializer, LocationSerializer
from listings.models import SpotFix, Location
from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 12


class SpotFixList(viewsets.ModelViewSet):
    queryset = SpotFix.objects.all()
    serializer_class = SpotFixSerializer
    pagination_class = StandardResultsSetPagination


class LocationList(viewsets.ModelViewSet):

    queryset = SpotFix.objects.all()
    serializer_class = SpotFixSerializer
    distance_filter_field = 'point'
    pagination_class = StandardResultsSetPagination
    filter_backends = (DistanceToPointFilter, )
    bbox_filter_include_overlapping = True
    # Optional


def index(request):
    spotfixes = SpotFix.objects.order_by('-planned_date')
    context = {'spotfixes': spotfixes}
    return render(request, 'listings/index.html', context)
