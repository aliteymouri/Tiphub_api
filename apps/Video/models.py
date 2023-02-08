from apps.Account.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField("عنوان دسته بندی مرجع ", max_length=50, unique=True)
    created_at = models.DateTimeField("تاریخ ایجاد در ", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مرجع"
        verbose_name_plural = "دسته بندی های مرجع "


class SubCategory(models.Model):
    category = models.ManyToManyField(Category, related_name="subcategories", verbose_name="زیرمجموعه دسته بندی ")
    title = models.CharField("عنوان دسته بندی ", max_length=50, unique=True)
    is_active = models.BooleanField("وضعیت ", default=True)
    created_at = models.DateTimeField("تاریخ ایجاد در ", auto_now_add=True)

    def __str__(self):
        return F"{self.title}"

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Video(models.Model):
    title = models.CharField("عنوان ویدیو", max_length=100, )
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="منتشر کننده", null=True, blank=True)
    category = models.ManyToManyField(SubCategory, related_name='videos', verbose_name="دسته بندی ویدیو")
    video = models.FileField("آپلود ویدیو", upload_to='videos/')
    description = models.TextField("درباره ویدئو")
    video_cover = models.ImageField("کاور ویدیو", upload_to='banner')
    time = models.CharField("تایم ویدیو", blank=True, null=True, max_length=15)
    is_active = models.BooleanField("وضعیت ", default=True)
    created_at = models.DateTimeField("تاریخ انتشار در ", auto_now_add=True)
    updated_on = models.DateTimeField("تاریخ بروزرسانی در ", auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.id, self.title)

    class Meta:
        verbose_name = "ویدیو"
        verbose_name_plural = "ویدیوها"


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments', verbose_name="ویدیو")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="کاربر")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies',
                               verbose_name="زیرمجموعه")
    text = models.TextField("متن کامنت ", )
    is_active = models.BooleanField("وضعیت", default=True)
    created_at = models.DateTimeField("تاریخ ثبت در ", auto_now_add=True)

    def __str__(self):
        return F' نظر : {self.text[:30]} / توسط : {self.author.fullname}'

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        ordering = ('-created_at',)
