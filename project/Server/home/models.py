from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    studentid = models.IntegerField(max_length=8)
    email = models.CharField(max_length=50)
    password = models.IntegerField(max_length=20)

    def __str__(self):
        return self.name

class Admin(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    lastindex = models.IntegerField(max_length=20)

    def __str__(self):
        return self.email