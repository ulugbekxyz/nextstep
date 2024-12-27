from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    skills = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    job_type = models.CharField(max_length=50)  # 'one-day' or 'long-term'

class Job(models.Model):
    title = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)