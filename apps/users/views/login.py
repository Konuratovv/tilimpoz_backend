from rest_framework.response import Response
from rest_framework import generics
from ..serializers import LoginSerializer
from ..services.login import LoginService
from ..models import CustomUser as User


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        access_token, refresh_token = LoginService.login(request, User)
        return Response({'access_token': f'{access_token}', "refresh_token": f'{refresh_token}'})
