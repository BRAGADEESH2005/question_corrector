# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authentication.models import User
from evaluators_qpuploaders.models import Question_Papers
# Create your models here.

class Mentor(models.Model):
    UserID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Student(models.Model):
    UserID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Grade = models.IntegerField()
    Board = models.CharField(max_length=10)
    Mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)


class Recommended_QPs(models.Model):
    MentorID = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    QP_ID = models.ForeignKey(Question_Papers, on_delete=models.CASCADE)
    isDone = models.BooleanField()
    RecommendedTime = models.DateTimeField()
