from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    gender = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name+','+self.major+','+self.age

