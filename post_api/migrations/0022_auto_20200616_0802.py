# Generated by Django 2.2 on 2020-06-16 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0021_post_bookmarks'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='posttagrelation',
            unique_together={('post_id', 'tag_id')},
        ),
    ]
