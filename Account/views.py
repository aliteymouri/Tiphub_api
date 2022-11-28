from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import logout
from rest_framework import status
from .models import User


class UsersListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LogoutView(APIView):
    def get(self, req):
        logout(req)
        return Response('Logged out Successfully', status=status.HTTP_200_OK)
