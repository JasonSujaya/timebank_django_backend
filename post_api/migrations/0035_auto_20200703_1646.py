# Generated by Django 2.2 on 2020-07-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0034_auto_20200703_1641'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['id', 'category'], name='post_api_po_id_896b4e_idx'),
        ),
    ]