from django.db import models

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