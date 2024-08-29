from rest_framework.response import Response
from rest_framework import generics, status
from ..serializers import RegisterSerializer
from ..services import UserService
from ..models import CustomUser as User


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return Response(UserService.register(request, RegisterSerializer), status=status.HTTP_201_CREATED)
