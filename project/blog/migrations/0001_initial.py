# Generated by Django 3.0.6 on 2020-05-31 06:08

import ckeditor_uploader.fields
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
            name='AuthorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='author/')),
                ('about', models.TextField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], max_length=10)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('skype_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('is_draft', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.AuthorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('photo', models.ImageField(upload_to='category/')),
                ('about', models.TextField()),
                ('is_draft', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.AuthorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=245, unique=True)),
                ('urltitle', models.CharField(max_length=100, unique=True)),
                ('language', models.CharField(choices=[('english', 'English'), ('bangla', 'Bangla')], max_length=20)),
                ('photo', models.ImageField(upload_to='post/')),
                ('shortTxt', models.TextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_draft', models.BooleanField(default=False)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('show', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.AuthorProfile')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.PostCategory')),
                ('tag', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
