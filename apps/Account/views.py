from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .serializers import UserSerializer, ChangePasswordSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from rest_framework.permissions import IsAuthenticated
from django.template.loader import render_to_string
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import login, logout
from .tokens import account_activation_token
from rest_framework.response import Response
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework import status
from .models import User


class SignUpView(CreateAPIView):
    def post(self, req, *args):
        ser = UserSerializer(data=req.data)
        if ser.is_valid():
            user = ser.save()
            user.is_active = False
            user.save()

            current_site = get_current_site(self.request)
            mail_subject = 'لینک فعالسازی حساب کاربری'
            message = render_to_string('emails/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = ser.validated_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return Response({"message": 'ایمیلی حاوی یک لینک جهت فعالسازی حساب کاربریتان ارسال شد'},
                            status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status.HTTP_400_BAD_REQUEST)


class Activate(APIView):
    def get(self, req, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(req, user)
            return Response("ثبت نام انجام شد")
        else:
            return Response("لینک وارد شده منقضی شده است لطفا دوباره تلاش کنید")


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
            return Response("عملیات با موفقیت انجام شد", status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPanelView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        ser = UserSerializer(instance=req.user)
        return Response(ser.data, status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    model = User

    def update(self, req, *args, **kwargs):
        user = req.user
        serializer = self.get_serializer(data=req.data)
        if serializer.is_valid():
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response("گذرواژَه تان با موفقیت تغییر کرد", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, req):
        logout(req)
        return Response(status=status.HTTP_200_OK)
