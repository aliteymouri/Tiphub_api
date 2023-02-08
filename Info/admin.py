from django.contrib import admin
from . import models


@admin.register(models.BeTeacher)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
