# Generated by Django 4.1.7 on 2023-03-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(max_length=100)),
                ('photo', models.ImageField(upload_to='flowers')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
