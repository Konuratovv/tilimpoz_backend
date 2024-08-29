from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser as User
from .services import UserService


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'confirm_password',
        ]

    def validate(self, data):
        return UserService.confirm_password_validator(data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


class VerifyEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['code', 'email']

class TopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'points']


class SendResetCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('code', )


class CheckResetCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'code', )


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)
    email = serializers.EmailField()
