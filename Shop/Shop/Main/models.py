from django.db import models

# Create your models here.

class Flowers(models.Model):

    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='flowers')
    quantity = models.PositiveIntegerField()
    slug = models.SlugField(max_length=50, default=' ')

    def __str__(self):
        return self.name

