from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    referal = models.CharField(max_length=20, default='default')
    people_invited_number = models.PositiveIntegerField(default=0)

    def add_new_member(self):
        self.people_invited_number += 1
        self.save()


class ReferalTable(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    referal_for_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='referal_for_user')
    rating = models.PositiveIntegerField(default=0)