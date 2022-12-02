from django.contrib.auth import password_validation
from rest_framework import serializers
from persiantools.jdatetime import JalaliDate
from Account.models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'user_permissions', 'groups', 'is_superuser')

    def get_date_joined(self, obj):
        return JalaliDate(obj.date_joined, locale=('fa')).strftime("%c")

    def validate_phone(self, value):
        if value[:2] != "09" or len(value) < 11:
            raise serializers.ValidationError('یک شماره تماس معتبر وارد کنید')
        return value


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Your old password was entered incorrectly. Please enter it again.')
        return value
