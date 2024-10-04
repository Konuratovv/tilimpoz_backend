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
    
    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("Нужно ввести ФИО")
        
        parts = value.split()
        if len(parts) < 2:
            raise serializers.ValidationError("Вам нужно ввести и имя и фамилию")
        
        for part in parts:
            if not part.isalpha():
                raise serializers.ValidationError("Ваше имя и фамилия не должны иметь ни одного символа кроме букв")
        
        return value            


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
        fields = ('email', )


class CheckResetCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'code', )


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    

class CurrentUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username')
        
class LogOutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
