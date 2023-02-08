from rest_framework import serializers
from Info.models import BeTeacher


class BeTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeTeacher
        fields = '__all__'

    def validate_phone(self, value):
        if value[:2] != "09" or len(value) < 11:
            raise serializers.ValidationError('یک شماره تماس معتبر وارد کنید')
        return value
