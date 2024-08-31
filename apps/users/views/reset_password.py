from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import mixins

from ..serializers import SendResetCodeSerializer, CheckResetCodeSerializer, ResetPasswordSerializer
from ..services import UserService

class SendResetCodeAPIView(generics.CreateAPIView):
    serializer_class = SendResetCodeSerializer

    def post(self, request, *args, **kwargs):
        email = self.request.data.get('email')
        return UserService.send_reset_code(email)
    

class CheckResetCodeAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = CheckResetCodeSerializer

    def patch(self, request, *args, **kwargs):
        email = self.request.data.get('email')
        code = self.request.data.get('code')
        return UserService.check_reset_code(email, code)
    
class ResetPasswordAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        new_password = self.request.data.get('new_password')
        confirm_password = self.request.data.get('confirm_password')
        email = self.request.data.get('email')
        message = UserService.reset_password(new_password, confirm_password, email)
        return Response({'message': f'{message}'}, status=status.HTTP_200_OK)