from django.utils.crypto import get_random_string
from django.conf import settings
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .models import CustomUser

class UserService:
    __user = CustomUser.objects.all()
    __generated_code = get_random_string(6, '0123456789')

    @classmethod
    def give_tokens_for_user(cls, user):
        return AccessToken.for_user(user), RefreshToken.for_user(user)

    @classmethod
    def send_verification_mail(cls, email):
        user = cls.__user.filter(email=email).first()
        user.code = cls.__generated_code
        user.save()
        subject = 'Your verification code'
        message = f'Your verification code:\n{cls.__generated_code}\nThanks for using our application.'
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, (email, ))

    @classmethod
    def register(cls, request, serializer_class):
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_instance = CustomUser.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
        )

        return {'status': 'success'}
    
    @classmethod
    def login(cls, email, password):

        user_instance = cls.__user.filter(email=email).first()

        if user_instance is None:
            raise AuthenticationFailed('User not found!')

        elif not user_instance.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        return cls.give_tokens_for_user(user_instance)
    
    @classmethod
    def confirm_password_validator(cls, data):
        if data.get('password') != data.get('confirm_password'):
            raise AuthenticationFailed(detail='Passwords do not match', code='password_mismatch')
        return data
    
    @classmethod
    def send_reset_code(cls, email):
        try:
            user = cls.__user.filter(email=email).first()
            cls.send_verification_mail(user.email)
            return Response({"message": "Код жиберилди!"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message": "Электрондук почта катталбаган"}, status=status.HTTP_400_BAD_REQUEST)
        
    @classmethod
    def check_reset_code(cls, email, verify_code):
        try:
            user = cls.__user.filter(email=email).first()
            if verify_code == user.code:
                user.code = None
                user.save()
                return Response({"message": "Код туура!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Код туура эмес!"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Туура эмес!!!!"}, status=status.HTTP_400_BAD_REQUEST)
        
    @classmethod
    def reset_password(cls, new_password, confirm_password, email):
        if new_password == confirm_password:
            user = cls.__user.filter(email=email).first()
            user.password = make_password(confirm_password)
            user.save()
            return "Success"
        else:
            return "Passwords did not match"






