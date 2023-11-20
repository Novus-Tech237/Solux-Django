from django.contrib import admin
from django.urls import path
from .views import *

app_name = "tutos"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('vscode/', VSCodeTutoView.as_view(), name="vscode"),
    path('html/introduction', HtmlIntroductionView.as_view(), name="html_introduction"),
    path('html/structure', HtmlStructureView.as_view(), name="html_structure"),
    path("html/text_formating", HtmlTextFormatingView.as_view(), name="html_textformating")
    
]