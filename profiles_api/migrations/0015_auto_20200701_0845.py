# Generated by Django 2.2 on 2020-07-01 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0014_auto_20200701_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileimage',
            name='alt_text',
        ),
        migrations.RemoveField(
            model_name='profileimage',
            name='description',
        ),
    ]
