# Generated by Django 4.1.7 on 2023-03-21 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_customuser_people_invited_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferalTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0)),
                ('referal_for_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referal_for_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]