# Generated by Django 2.2.24 on 2021-10-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
