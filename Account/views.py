from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from .models import User


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EditProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req, pk):
        instance = User.objects.get(id=pk)
        ser = UserSerializer(instance=instance, data=req.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response("User Information Updated Successfully", status=status.HTTP_200_OK)
        return Response(ser.errors)


class LogoutView(APIView):
    def get(self, req):
        logout(req)
        return Response('Logged out Successfully', status=status.HTTP_200_OK)
