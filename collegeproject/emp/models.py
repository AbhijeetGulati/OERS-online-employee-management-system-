from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


#creating seperate class for dept and we will link it later using foreign key
class Dept(models.Model):
    name=models.CharField(max_length=100,null=False)
    

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name
# Create your models here.
class Employee(models.Model):
    
    first_name=models.CharField(max_length=100,null=False)  #first name cant be empty
    last_name=models.CharField(max_length=100)
    #linking department using foreign key
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
    #salary and bonus will be both integer values
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    

    def __str__(self):
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)