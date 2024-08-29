from rest_framework.response import Response
from rest_framework import generics
from ..serializers import LoginSerializer
from ..services import UserService
from ..models import CustomUser as User


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        access_token, refresh_token = UserService.login(email, password)
        return Response({'access_token': f'{access_token}', "refresh_token": f'{refresh_token}'})
