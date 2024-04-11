# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from students_mentors.models import Student
from evaluators_qpuploaders.models import Evaluator, Question_Papers, QP_Structure

# Create your models here.
class Evaluations(models.Model):
    StudentID = models.ForeignKey(Student,on_delete=models.CASCADE)
    EvaluatorID = models.ForeignKey(Evaluator,on_delete=models.CASCADE)
    EvaluationID = models.CharField(max_length=10,primary_key= True)
    PaperID = models.ForeignKey(Question_Papers,on_delete=models.CASCADE)
    Marks = models.IntegerField()
    UploadTime = models.DateTimeField()
    Student_Rating = models.IntegerField()
    Evaluator_Rating = models.IntegerField()


class Evaluated_Questions(models.Model):
    EvaluationID = models.ForeignKey(Evaluations,on_delete=models.CASCADE)
    QP_ID = models.ForeignKey(Question_Papers,on_delete=models.CASCADE)
    GroupMarks = models.ForeignKey(QP_Structure,on_delete=models.CASCADE)
    QuestionNumber = models.CharField(max_length=10)
    Marks = models.IntegerField()
    Feedback = models.CharField(max_length=100)
