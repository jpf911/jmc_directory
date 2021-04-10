from django.db import models

# Create your models here.
class Student(models.Model):
    First_name=models.CharField(max_length=200)
    Last_name=models.CharField(max_length=200)
    Email=models.CharField(max_length=50)
    Contact=models.IntegerField()
    Address=models.CharField(max_length=200)
    Course=models.CharField(max_length=10)
    def __str__(self):
         return self.First_name

class Teacher(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Email = models.CharField(max_length=50)
    Contact = models.IntegerField()
    Address = models.CharField(max_length=200)
    Course = models.CharField(max_length=10)
    def __str__(self):
         return self.First_name
