# Generated by Django 4.1.3 on 2022-11-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0002_alter_video_publisher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='about_video',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='video_time',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='video',
            name='slug',
        ),
        migrations.AlterField(
            model_name='video',
            name='video_cover',
            field=models.ImageField(upload_to='banner', verbose_name='کاور ویدیو'),
        ),
    ]
