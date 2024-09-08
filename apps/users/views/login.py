from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from ..serializers import LoginSerializer
from ..services import UserService

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "email",
                openapi.IN_FORM,
                description="email пользователя", 
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                "password",
                openapi.IN_FORM,
                description="пароль пользователя", 
                type=openapi.TYPE_STRING
            )
        ],
        operation_description="""
Авторизация, при правильном вводе, выдаются access и refresh токены
""",
        responses={200: "OK"}
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        access_token, refresh_token = UserService.login(email, password)
        return Response({'access_token': f'{access_token}', "refresh_token": f'{refresh_token}'})
