from django.db import models
from apps.Account.models import User
from persiantools.jdatetime import JalaliDate


class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification', verbose_name='فرستنده')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', verbose_name='کاربر')
    text = models.TextField('متن اعلان')
    created_at = models.DateTimeField('تاریخ ارسال در', auto_now_add=True)

    def __str__(self):
        return F" اعلان : {self.text} به کاربر : {self.user}"

    def jalali_date(self, obj):
        return JalaliDate(self.created_at, locale=('fa')).strftime('%c')

    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = 'اعلانات'
