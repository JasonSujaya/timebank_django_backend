# Generated by Django 2.2 on 2020-07-03 16:41

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timebanking_api', '0005_auto_20200701_1654'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='transaction',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created_date'], name='timebanking_created_21936c_brin'),
        ),
    ]