from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from persiantools.jdatetime import JalaliDate
from .managers import UserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("پست الکترونیک", max_length=120, unique=True)
    phone = models.CharField("شماره تماس ", max_length=11, unique=True, )
    fullname = models.CharField("نام و نام خانوادگی  ", max_length=80)
    image = models.ImageField(upload_to="users/profile", null=True, blank=True, verbose_name='عکس پروفایل ')
    bio = models.TextField("بیوگرافی ", null=True, blank=True, )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت نام ")
    github = models.URLField('آدرس گیت هاب', blank=True)
    linkedin = models.URLField('آدرس لینکدین', blank=True)
    instagram = models.URLField('آدرس اینستاگرام', blank=True)
    twitter = models.URLField('آدرس توییتر', blank=True)
    is_active = models.BooleanField("وضعیت ", default=True)
    is_admin = models.BooleanField("مدیر سایت  ", default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'phone']

    def __str__(self):
        return F" کاربر : {self.fullname}"

    def get_jalali_date(self):
        return JalaliDate(self.date_joined, locale=('fa')).strftime("%c")

    get_jalali_date.short_description = 'تاریخ ثبت نام'

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name_plural = 'کاربرها'
        verbose_name = 'کاربر'
