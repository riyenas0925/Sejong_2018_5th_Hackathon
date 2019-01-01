from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    studentid = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Admin(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    lastindex = models.IntegerField(default=0)
    cnt = models.IntegerField(default=500)

    def __str__(self):
        return self.email