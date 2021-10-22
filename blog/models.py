from django.conf import settings
from django.db import models
from django.utils import timezone


class Bike(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    img=models.ImageField()
    description=models.TextField()
    date=models.DateField()
    country=models.CharField(max_length=50)
    type=models.CharField(max_length=60)

   

    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    date=models.DateTimeField()
    img=models.ImageField()

class Parts(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    parameters=models.TextField()
    price=models.PositiveIntegerField()