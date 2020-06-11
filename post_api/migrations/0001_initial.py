# Generated by Django 2.2 on 2020-06-11 17:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ReportCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_api.Post')),
                ('tag_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post_api.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post_api.ReportCategory')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_api.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('alt_text', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_api.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_api.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_api.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post_api.PostCategory'),
        ),
        migrations.AddField(
            model_name='post',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CommentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post_api.ReportCategory')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_api.PostComment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
