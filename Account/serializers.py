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


