from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    due_date = models.DateField(null=True,blank=True)
    user = models.ForeignKey(User,max_length=10,on_delete=models.CASCADE,null=True)  
      

class user_view(models.Model):
    reviewer_name = models.CharField(max_length=200)
    reviewer_task = models.CharField(max_length=200)
    reviewer_due_date = models.DateField(null=True,blank=True)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
   


