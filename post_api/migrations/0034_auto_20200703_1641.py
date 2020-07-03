# Generated by Django 2.2 on 2020-07-03 16:41

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0033_auto_20200703_1635'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='post',
            name='post_api_po_categor_aefd09_brin',
        ),
        migrations.AddIndex(
            model_name='post',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created_date'], name='post_api_po_created_33cbc3_brin'),
        ),
    ]