from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login,logout
import time
from .forms import *
from django.urls import reverse, reverse_lazy
import boto3
from botocore.exceptions import NoCredentialsError
from django.conf import settings
from django.core.mail import EmailMessage
from .models import *

class AboutView(View):
    template_name = 'about.html'
    def get(self, request):
        return render(request, self.template_name)
class IndexView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)
class ServiceView(View):
    template_name = 'service.html'
    def get(self, request):
        return render(request, self.template_name)
class TestView(View):
    template_name = 'test.html'
    def get(self, request):
        return render(request, self.template_name)
class LogoutView(LoginRequiredMixin, View):
    success_url = reverse_lazy('user_auth:login')
    def get(self, request):
        time.sleep(2)
        logout(request)
        return redirect(self.success_url)  
class SalesView(LoginRequiredMixin, View):
    template_name = 'sales.html'
    def get(self, request):
        return render(request, self.template_name)
class ContactView(View):
    template_name = 'contact.html'
    def get(self, request):
        return render(request, self.template_name)
class SolutionView(LoginRequiredMixin, View):
    template_name = 'cover_page2.html'
    def get(self, request):
        return render(request, self.template_name)
