from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class UserAPIView(APIView):
    """
    View to list all users in the system.

    """
    def get(self, request, format=None):
        """
        Return a success message on successful configuration of django boiler plate.
        """
        return Response({
            "msg": "successfully installed django boiler plate"
        })