from django.contrib import admin
from django.urls import path
from .views import *

app_name = "alert"
urlpatterns = [
    path("error-login/", ErrorLoginView.as_view(), name="error-login"),
    path("error-register/",ErrorRegisterView.as_view(), name="error-register"),
    path("error-verification/",ErrorVerificationView.as_view(), name="error-verification"),
    path("error-database/",ErrorDatabaseView.as_view(), name="error-database"),
    path("error-reset_pass/", ErrorResetPasswordView.as_view(), name="error-reset_password"),
    
    path("notify-reset_password/", NotifyResetPasswordView.as_view(), name="notify-reset_password"),
    path("notify-email/",NotifyEmailView.as_view(), name="notify-email"),
    path("notify-register/", NotifyRegisterView.as_view(), name="notify-register"),
]