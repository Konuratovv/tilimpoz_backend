class RegistrationService:
    @classmethod
    def register(cls, request, user, serializer_class):
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_instance = user.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
        )

        return {'status': 'success'}
