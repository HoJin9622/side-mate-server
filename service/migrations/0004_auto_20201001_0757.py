# Generated by Django 2.2.12 on 2020-10-01 07:57

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=128, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='아이디'),
        ),
    ]