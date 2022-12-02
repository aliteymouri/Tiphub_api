from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ChangePasswordSerializer
from django.contrib.auth import logout
from rest_framework import status
from .models import User


class UsersListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EditProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req):
        ser = UserSerializer(instance=req.user, data=req.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response("User Info Updated Successfully", status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPanelView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        ser = UserSerializer(instance=req.user)
        return Response(ser.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def get(self, req):
        logout(req)
        return Response('Logged out Successfully', status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    model = User

<<<<<<< HEAD
    def update(self, req, *args, **kwargs):
        user = req.user
        serializer = self.get_serializer(data=req.data)
=======
    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
>>>>>>> 18bdf0486bd574d38f2e514d3f7198e7d0cde83d
        if serializer.is_valid():
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response("Password Updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
