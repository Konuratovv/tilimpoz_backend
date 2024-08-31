from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import GenericAPIView

from ..serializers import VerifyEmailSerializer
from ..services import UserService
from ..models import CustomUser

class VerifyEmailAPIView(UpdateModelMixin, GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def patch(self, request, *args, **kwargs):
        email = self.request.data.get('email')
        code = self.request.data.get('code')
        return UserService.verify_user(email, code)
