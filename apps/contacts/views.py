from rest_framework.permissions import AllowAny

from .models import Contact
from rest_framework.generics import ListAPIView

from .serializers import ContactSerializer


# Create your views here.

class ContactsListAPIView(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [AllowAny]