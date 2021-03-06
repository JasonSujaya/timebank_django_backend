# Generated by Django 2.2 on 2020-07-01 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post_interaction_api', '0007_auto_20200616_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postbookmark',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
