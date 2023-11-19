from django.contrib import admin
from django.urls import path
from .views import *

app_name = "tutos"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('vscode/', VSCodeTutoView.as_view(), name="vscode"),
    path('html/', HtmlTutoView.as_view(), name="html"),
    path('html/introduction', HtmlIntroductionView.as_view(), name="html_introduction"),
    path('html/description', HtmlDescriptionView.as_view(), name="html_description"),
    
]