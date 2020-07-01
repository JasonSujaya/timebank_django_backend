# Generated by Django 2.2 on 2020-07-01 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0007_auto_20200701_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='latest_consent',
        ),
        migrations.AddField(
            model_name='userconsent',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]