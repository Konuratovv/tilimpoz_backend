from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..models import CustomUser as User
from ..serializers import TopUserSerializer

class TopUsersAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        top_users = User.objects.order_by('-points')[:3]
        serializer = TopUserSerializer(top_users, many=True)
        return Response(serializer.data)
