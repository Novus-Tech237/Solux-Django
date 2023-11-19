from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration=models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.title 
# Create your models here.
