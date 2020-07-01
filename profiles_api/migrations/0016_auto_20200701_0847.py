# Generated by Django 2.2 on 2020-07-01 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0015_auto_20200701_0845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='user_profile',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='profileimage',
            old_name='user_profile',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userconsent',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='userconsent',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
