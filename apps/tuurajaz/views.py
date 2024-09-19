from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import TuuraJazModel
from .serializers import TuuraJazSerializer, TuuraJazDetailedSerializer

class TuuraJazListAPIView(generics.ListAPIView):
    queryset = TuuraJazModel.objects.all()
    serializer_class = TuuraJazSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TuuraJazDetailedAPIView(generics.RetrieveAPIView):
    queryset = TuuraJazModel.objects.all()
    serializer_class = TuuraJazDetailedSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )



