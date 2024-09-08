from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotAuthenticated

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..models import CustomUser as User
from ..serializers import TopUserSerializer
from ..services import UserService

class TopUsersAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        
        operation_description="""Тут если пользователь не авторизован, то выводится без текщего пользователя, а если
        авторизован, то выводится 50 пользователей по ключу top_users и текщий пользователь и его позиция по ключу current_user 
        """,
        responses={200: "OK"}
    )
    def get(self, request):
        return UserService.top_users(request, TopUserSerializer)
