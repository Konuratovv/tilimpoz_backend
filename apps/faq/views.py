from django.shortcuts import render
from rest_framework import generics

from .models import Faq
from .serializers import FaqSerializer


# Create your views here.


class FaqListAPIView(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer