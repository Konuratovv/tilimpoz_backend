from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError, AuthenticationFailed


class PasswordValidator:
    @classmethod
    def confirm_password_validator(cls, data):
        if data.get('password') != data.get('confirm_password'):
            raise AuthenticationFailed(detail='Passwords do not match', code='password_mismatch')
        return data
