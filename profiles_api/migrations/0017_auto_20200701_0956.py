# Generated by Django 2.2 on 2020-07-01 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0016_auto_20200701_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles_api.Country'),
        ),
    ]
