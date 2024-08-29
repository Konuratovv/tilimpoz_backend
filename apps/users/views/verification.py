from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView

from ..serializers import VerifyEmailSerializer
from ..services import UserService

class VerifyEmailAPIView(UpdateAPIView):
    serializer_class = VerifyEmailSerializer

    def patch(self, request, *args, **kwargs):
        email = self.request.data.get('email')
        code = self.request.data.get('code')
        return UserService.verify_user(email, code)
