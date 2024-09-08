from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..serializers import RegisterSerializer
from ..services import UserService
from ..models import CustomUser as User


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "username",
                openapi.IN_FORM,
                description="Имя пользователя", 
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                "email",
                openapi.IN_FORM,
                description="email пользователя", 
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                "password",
                openapi.IN_FORM,
                description="Пароль", 
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                "confirm_password",
                openapi.IN_FORM,
                description="Подтвердить пароль", 
                type=openapi.TYPE_STRING
            ),
        ],
        operation_description="""
Регистрация. Я сделал валидацию на username чтобы он вводил именно имя и фоамилию а не один никнейм, 
потому что в дизайне я видел что там было написано сокращенно Тилек М. и в форме было написано "Аты-жону", что я подумал сделать такую валидацию,
если она не нужна то я уберу, скорее всего у Азизы надо спросить <3 
""",
        responses={201: "success, этот код отвечает за то что обьект успешно создан"}
    )
    def post(self, request, *args, **kwargs):
        return Response(UserService.register(request, RegisterSerializer), status=status.HTTP_201_CREATED)
