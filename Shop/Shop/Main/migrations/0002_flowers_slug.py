# Generated by Django 4.1.7 on 2023-03-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='slug',
            field=models.SlugField(default=' '),
        ),
    ]