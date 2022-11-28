from rest_framework import serializers
from persiantools.jdatetime import JalaliDate
from Account.models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'user_permissions', 'groups')

    def get_date_joined(self, obj):
        return JalaliDate(obj.date_joined, locale=('fa')).strftime("%c")
