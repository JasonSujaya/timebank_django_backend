# Generated by Django 2.2 on 2020-07-03 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0043_auto_20200703_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
