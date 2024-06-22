# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from authentication.models import User
from django.core.exceptions import ValidationError

def validate_pdf(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")

# Create your models here.
class QP_Uploader(models.Model):
    UserID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Evaluator(models.Model):
    UserID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Rating = models.IntegerField()

class Eval_Languages(models.Model):
    UserID = models.ForeignKey(Evaluator,on_delete=models.CASCADE)
    Language = models.CharField(max_length=10)

class Eval_Subjects(models.Model):
    UserID = models.ForeignKey(Evaluator,on_delete=models.CASCADE)
    Subject = models.CharField(max_length=10)

class Eval_Boards(models.Model):
    UserID = models.ForeignKey(Evaluator,on_delete=models.CASCADE)
    Board = models.CharField(max_length=10)

class Question_Papers(models.Model):
    QP_ID = models.CharField(max_length=10,primary_key= True)
    QP_Name = models.CharField(max_length=50)
    QP_UploaderID = models.ForeignKey(QP_Uploader,on_delete=models.CASCADE)
    QP_UploadDate = models.DateField()
    QP_Subject = models.CharField(max_length=10)
    QP_Language = models.CharField(max_length=10)
    QP_Board = models.CharField(max_length=10)
    QP_Grade = models.IntegerField()
    QP_File = models.FileField(upload_to='question_papers',validators=[validate_pdf])


class QP_Structure(models.Model):
    QP_ID = models.ForeignKey(Question_Papers,on_delete=models.CASCADE)
    Group_Marks = models.IntegerField()
    Group_Size = models.IntegerField()

