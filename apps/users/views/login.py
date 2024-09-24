from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status
from rest_framework import exceptions
from ..serializers import LoginSerializer, CurrentUserSerializer
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
    
    
class RetrieveCurrentUserAPIView(generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        try:
            current_user = self.request.user
            return Response(self.get_serializer(current_user).data, status=status.HTTP_200_OK)
        except exceptions.NotAuthenticated:
            return Response({'message': 'You are not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
                
