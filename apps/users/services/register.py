class RegistrationService:
    @classmethod
    def register(cls, request, user, serializer):
        ser = serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user_instance = user.objects.create_user(
            username=ser.validated_data['username'],
            email=ser.validated_data['email'],
            password=ser.validated_data['password'],
        )
        return {'status': 'success'}
