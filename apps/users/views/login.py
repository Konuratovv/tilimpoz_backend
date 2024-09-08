from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import generics
from ..serializers import LoginSerializer
from ..services import UserService

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    parser_classes = (MultiPartParser, JSONParser)

    @swagger_auto_schema(
        operation_description="""
Авторизация, при правильном вводе, выдаются access и refresh токены
""",
        request_body=LoginSerializer,
        responses={200: "OK"}
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        access_token, refresh_token = UserService.login(email, password)
        return Response({'access_token': f'{access_token}', "refresh_token": f'{refresh_token}'})
