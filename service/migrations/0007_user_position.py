# Generated by Django 2.2.12 on 2020-10-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_post_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='포지션'),
        ),
    ]
