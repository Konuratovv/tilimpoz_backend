from django.shortcuts import render
from rest_framework import generics
from .models import SabattuuModel
from .serializers import SabattuuJoobtorListSerializer, SabattuuJoobtorDetailedSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class SabattuuJoobtorListAPIView(generics.ListAPIView):
    queryset = SabattuuModel.objects.all()
    serializer_class = SabattuuJoobtorListSerializer


class SabattuuJoobtorDetailedAPIView(generics.RetrieveAPIView):
    queryset = SabattuuModel.objects.all()
    serializer_class = SabattuuJoobtorDetailedSerializer


