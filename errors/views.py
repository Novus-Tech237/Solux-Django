from django.shortcuts import render
from django.views import View

class ErrorLoginView(View):
    template_name = 'error_login.html'
    def get(self, request):
        return render(request, self.template_name)
class ErrorRegisterView(View):
    template_name = 'error_register.html'
    def get(self, request):
        return render(request, self.template_name)
class ErrorVerificationView(View):
    template_name = 'error_verification.html'
    def get(self, request):
        return render(request, self.template_name)
class ErrorDatabaseView(View):
    template_name = 'error_database.html'
    def get(self, request):
        return render(request, self.template_name)
class ErrorResetPasswordView(View):
    template_name = 'error_reset-password.html'
    def get(self, request):
        return render(request, self.template_name)
    
class NotifyEmailView(View):
    template_name = 'notify_email.html'
    def get(self, request):
        return render(request, self.template_name)
class NotifyRegisterView(View):
    template_name = 'notify_registration.html'
    def get(self, request):
        return render(request, self.template_name)
class NotifyResetPasswordView(View):
    template_name = 'notify_reset-password.html'
    def get(self, request):
        return render(request, self.template_name)
# Create your views here.
