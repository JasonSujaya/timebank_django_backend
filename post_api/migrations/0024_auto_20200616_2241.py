# Generated by Django 2.2 on 2020-06-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0023_auto_20200616_2232'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['category'], name='post_api_po_categor_f13fac_idx'),
        ),
    ]