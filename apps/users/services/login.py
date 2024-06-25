from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class LoginService:
    @classmethod
    def login(cls, request, user):
        user_instance = user.objects.filter(email=request.data.get('email')).first()

        if user_instance is None:
            raise AuthenticationFailed('User not found!')

        if not user_instance.check_password(request.data.get('password')):
            raise AuthenticationFailed('Incorrect password!')

        if not user_instance.is_verified:
            raise AuthenticationFailed('User is not verified!')

        access_token = AccessToken.for_user(user_instance)
        refresh_token = RefreshToken.for_user(user_instance)

        return access_token, refresh_token
