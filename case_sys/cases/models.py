from django.db import models

# Create your models here.

class Case(models.Model):
    case_id = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=100)
    case_description = models.TextField()
    case_status = models.CharField(max_length=50)
    case_priority = models.CharField(max_length=50)
    case_assignee = models.CharField(max_length=50)
    case_created = models.DateTimeField(auto_now_add=True)
    case_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_name
    

class Courts(models.Model):
    court_id = models.AutoField(primary_key=True)
    court_name = models.CharField(max_length=100)
    court_location = models.CharField(max_length=100)
    court_created = models.DateTimeField(auto_now_add=True)
    court_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.court_name
    
class Judges(models.Model):
    judge_id = models.AutoField(primary_key=True)
    judge_name = models.CharField(max_length=100)
    judge_court = models.ForeignKey(Courts, on_delete=models.CASCADE)
    judge_started = models.DateTimeField(auto_now_add=False)
    judge_ended = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.judge_name