# Generated by Django 2.2 on 2020-06-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_auto_20200616_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='alt_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='image_path',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]