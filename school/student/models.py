from django.db import models
from tkinter import CASCADE
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=250)

class AddCourses(models.Model):
    course = models.CharField(max_length=200)
    fees = models.IntegerField()
    duration = models.CharField(max_length=200,default='1')
    desc = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course  
    
class AddStudents(models.Model):
    sname = models.CharField(max_length=255,null=True,blank=True)
    semail = models.EmailField(max_length=255,null=True,blank=True)
    smobile = models.IntegerField(default='0',null=True,blank=True)
    scollege = models.CharField(max_length=255,default='anything')
    sdegree = models.CharField(max_length=255,default='anything') 
    saddress = models.CharField(max_length=255,default='0',null=True,blank=True)
    scourses = models.ForeignKey(AddCourses, on_delete=models.CASCADE,default='0',null=True,blank=True)
    
    def __str__(self):
        return self.sname
     
class AddTeacher(models.Model):
    tname = models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric])
    temail = models.EmailField(max_length=100)
    tmobile = models.IntegerField()
    taddress= models.CharField(max_length=255)
    experience = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.tname