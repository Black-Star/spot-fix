from rest_framework import generics
from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import viewsets

from listings.serializers import SpotFixSerializer
from listings.models import SpotFix
from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 12


class SpotFixList(viewsets.ModelViewSet):
    queryset = SpotFix.objects.all()
    serializer_class = SpotFixSerializer
    pagination_class = StandardResultsSetPagination


def index(request):
    spotfixes = SpotFix.objects.order_by('-planned_date')
    context = {'spotfixes': spotfixes}
    return render(request, 'listings/index.html', context)
