from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class LoginService:
    @classmethod
    def login(cls, request, user):
        email = request.data.get('email')
        password = request.data.get('password')

        user_instance = user.objects.filter(email=email).first()

        if user_instance is None:
            raise AuthenticationFailed('User not found!')

        elif not user_instance.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        elif not user_instance.is_verified:
            raise AuthenticationFailed('User is not verified!')

        access_token, refresh_token = AccessToken.for_user(user_instance), RefreshToken.for_user(user_instance)

        return access_token, refresh_token
