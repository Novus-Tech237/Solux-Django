from django.contrib import admin
from django.urls import path
from .views import *

app_name = "user_auth"
urlpatterns = [
    path('login', UserLogin.as_view(), name="login"),
    path('registration/',RegisterView.as_view(),name='register'),
    path('forgot_password',ForgotPasswordView.as_view(),name='forgot_password'),
]
