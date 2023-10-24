from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse, reverse_lazy
from .models import *
from .helpers import *
import uuid
from django.conf import settings
import time
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(View):
    template_name = 'register.html'
    success_url = reverse_lazy('errors:notify-register')
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = request.POST
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        email = data['email']
        password = data['password']
        try:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user.save()
            return redirect(self.success_url)
        except:
            return redirect(self.template_name)
class UserLogin(View):
    template_name = 'login.html'
    success_url = reverse_lazy('shop:sales')
    admin_template_name = reverse_lazy('shop:test')
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect(self.admin_template_name)
            else:
                return redirect(self.success_url)
        else:
            return render(request, self.template_name)
 
class ForgotPasswordView(View): 
    template_name = 'forgot_password.html'
    error_url = reverse_lazy('errors:error-database')
    notify_url = reverse_lazy('errors:notify-email')
    def get(self, request):
        return render(request, self.template_name)
    # def post(self, request):
    #     data = request.POST
    #     email = data.get('email')
    #     user = User.objects.filter(email=email).first()
    #     if not user:
    #         return redirect(self.error_url)
    #     user_obj = User.objects.get(email=email)
    #     token = str(uuid.uuid4())
    #     profile_obj = Profile.objects.get(user=user_obj)
    #     profile_obj.forget_password_token = token
    #     profile_obj.save()
    #     send_forget_mail(email, token)
    #     return redirect(self.notify_url)
class ResetPasswordView(View):
    template_name = 'password_reset.html'
    error_url = reverse_lazy('errors:error-reset_password')
    notify_url = reverse_lazy('errors:notify-reset_password')
    def get(self, request, token):
        context = {'token': token}
        return render(request, self.template_name, context)
    # def post(self, request, token):
    #     data = request.POST
    #     context = {'token': token}
    #     new_password = data.get('new_password')
    #     confirm_password = data.get('confirm_password')
    #     if new_password != confirm_password:
    #         return render(request, str(self.error_url), context)
    #     try:
    #         profile_obj = Profile.objects.get(forget_password_token=token)
    #     except Profile.DoesNotExist:
    #         return render(request, str(self.error_url), context)
    #     user = profile_obj.user
    #     user.set_password(new_password)
    #     user.save()
    #     profile_obj.forget_password_token = None
    #     profile_obj.save()
    #     return redirect(str(self.notify_url))
# Create your views here.
