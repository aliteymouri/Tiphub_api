# Generated by Django 4.1.3 on 2022-11-11 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='منتشر کننده'),
        ),
    ]
