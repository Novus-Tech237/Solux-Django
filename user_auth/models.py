from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import uuid

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    forget_password_token = models.CharField(max_length=100, null=True, blank=True)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    def __str__(self):
        return self.user.username
class Researcher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + "(Researcher)"
    
