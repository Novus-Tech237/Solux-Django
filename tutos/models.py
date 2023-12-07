from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    topics = models.CharField(max_length=1000000)
    price = models.IntegerField()
    lessons = models.IntegerField()
    level = models.CharField(max_length=30)
    lesson_type = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    oversight = models.CharField(max_length=10000)
    lecturer = models.CharField(max_length=50)
    about_lecturer = models.CharField(max_length=50000)
    language = models.CharField(max_length=30)
    learning_objectives = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='course_images/')
    def __init__(self):
        return self.title