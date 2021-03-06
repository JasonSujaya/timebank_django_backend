# Generated by Django 2.2 on 2020-07-01 08:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0012_auto_20200701_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 8, 41, 57, 52398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userconsent',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 8, 41, 57, 51307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 8, 41, 57, 46274, tzinfo=utc)),
        ),
    ]
