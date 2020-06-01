# Generated by Django 3.0.6 on 2020-05-31 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('fb', models.URLField(blank=True, null=True)),
                ('tw', models.URLField(blank=True, null=True)),
                ('gh', models.URLField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mypic1', models.ImageField(upload_to='sitesettings/')),
                ('mypic2', models.ImageField(upload_to='sitesettings/')),
                ('mypic3', models.ImageField(upload_to='sitesettings/')),
                ('mypic4', models.ImageField(upload_to='sitesettings/')),
                ('loge', models.ImageField(upload_to='sitesettings/')),
            ],
        ),
    ]
