# Generated by Django 2.2 on 2020-06-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0020_auto_20200616_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
