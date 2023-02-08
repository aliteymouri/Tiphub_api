from django.contrib import admin
from . import models


@admin.register(models.Notification)
class AdminPersonalNotification(admin.ModelAdmin):
    list_display = ("__str__", "sender")
    list_filter = ("created_at", "sender")
    search_fields = ("user",)
