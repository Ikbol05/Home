from django.shortcuts import render
from rest_framework import viewsets
from . models import Region, Organizaytion, Building
from . serializer import RegionSerializer, OrganizationSerializer, BuildingSerializer
# Create your views here.

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organizaytion.objects.all()
    serializer_class = OrganizationSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer