from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.user_agent_generator import UserAgentService
from api.serializers import UserAgentRequestSerializer


class UserAgentGeneratorView(APIView):
    def post(self, request):
        serializer = UserAgentRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        service = UserAgentService()

        try:
            user_agents = service.generate_user_agents(
                os_type=data['os_type'].lower(),
                browser=data['browser'].lower(),
                count=data['count'],
                unique=data['unique']
            )
            return Response({"user_agents": user_agents}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)