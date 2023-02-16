from rest_framework import serializers
from apps.Info.models import BeTeacher
from apps.Account.forms import validate_phone


class BeTeacherSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[validate_phone])

    class Meta:
        model = BeTeacher
        fields = '__all__'
