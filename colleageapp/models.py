from django.db import models

class faculty1(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    qualificaton=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

class student1(models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    semail=models.EmailField(max_length=50)
    unquieid=models.IntegerField()




