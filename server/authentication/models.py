# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=100)

class Admin(models.Model):
    UserID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
