# Generated by Django 2.2 on 2020-06-16 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0022_auto_20200616_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookmarks',
            field=models.IntegerField(default=0),
        ),
    ]
