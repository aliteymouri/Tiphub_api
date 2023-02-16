from persiantools.jdatetime import JalaliDate
from apps.Account.forms import validate_phone
from rest_framework import serializers
from apps.Account.models import User


class UserSerializer(serializers.ModelSerializer):
    notifications = serializers.StringRelatedField(many=True, read_only=True)
    date_joined = serializers.SerializerMethodField(read_only=True)
    phone = serializers.CharField(validators=[validate_phone])

    class Meta:
        model = User
        fields = '__all__'

    def get_date_joined(self, obj):
        return JalaliDate(obj.date_joined, locale=('fa')).strftime("%c")


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("رمزعبور مشابه نمیباشد")
        return data

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('گذرواژه فعلی تان اشتباه وارد شد. لطفا مجدد تلاش کنید')
        return value
