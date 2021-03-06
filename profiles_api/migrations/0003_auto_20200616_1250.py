# Generated by Django 2.2 on 2020-06-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20200616_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileimage',
            old_name='user_id',
            new_name='user_profile',
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
