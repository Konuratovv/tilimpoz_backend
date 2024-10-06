from django.shortcuts import render

from rest_framework import generics

from . import serializers, models

# Create your views here.


class PartnersListAPIView(generics.ListAPIView):
    serializer_class = serializers.PartnersSerialzer
    queryset = models.Partner.objects.all()
