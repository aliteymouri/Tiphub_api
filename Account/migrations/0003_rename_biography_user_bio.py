# Generated by Django 4.1.3 on 2022-11-13 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_rename_phone_number_user_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='biography',
            new_name='bio',
        ),
    ]
