# Generated by Django 2.2 on 2020-07-01 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0029_auto_20200701_1025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostTag',
            new_name='Tag',
        ),
    ]
