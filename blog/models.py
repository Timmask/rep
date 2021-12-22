from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User

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
class Card(models.Model):
    bike=ForeignKey(Bike,on_delete=CASCADE,default=None)
    user=ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

class Parts(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    parameters=models.TextField()
    price=models.PositiveIntegerField()
    
class Stuff(models.Model):
    fullname=models.CharField(max_length=80)
    role=models.CharField(max_length=50)
    description=models.TextField()
    email=models.EmailField()
    img=models.ImageField()
    def __str__(self):
        return self.fullname
# class Question(models.Model):
#     author=ForeignKey(User,on_delete=CASCADE)
#     text=models.TextField()
