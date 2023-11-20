from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.hashers import make_password
from tutos.models import Course
class Student(User):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    progress = models.PositiveIntegerField(default=0)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    forget_password_token = models.CharField(max_length=100, null=True, blank=True)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    def __str__(self):
        return self.user.username + 'Profile'
