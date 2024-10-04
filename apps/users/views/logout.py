from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..services import UserService
from ..serializers import LogOutSerializer

class LogOutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    
    @swagger_auto_schema(
        request_body=LogOutSerializer,
        responses={200: "Logged out successfuly"}
    )
    def post(self, request, *args, **kwargs):
        refresh_token = self.request.data['refresh_token']
        status = UserService.logout(refresh_token)
        return Response(status, status=HTTP_200_OK)