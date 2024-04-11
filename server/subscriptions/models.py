# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from students_mentors.models import Student
# Create your models here.
class Subscriptions(models.Model):
    SubscriptionID = models.CharField(max_length=10)
    UserID = models.ForeignKey(Student,on_delete=models.CASCADE)
    Sub_Type = models.Choices('Monthly','Yearly') # placeholder
    SubscriptionStartDate = models.DateField()
    SubscriptionEndDate = models.DateField()
    isOver = models.BooleanField() # can be derived from End Date instead