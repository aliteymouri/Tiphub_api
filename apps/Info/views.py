from rest_framework.generics import CreateAPIView
from .serializers import BeTeacherSerializer
from rest_framework.response import Response
from rest_framework import status


class BeTeacherView(CreateAPIView):
    def post(self, req, *args):
        ser = BeTeacherSerializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response({'message': 'اطلاعات شما با موفقیت ارسال شد'}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
