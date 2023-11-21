from django.contrib import admin
from django.urls import path
from .views import *

app_name = "tutos"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('vscode/introduction', VSCodeIntroductionView.as_view(), name="vscode_introduction"),
    path("vscode/extension", VSCodeExtensionView.as_view(), name="vscode_extension"),
    
    path('html/introduction', HtmlIntroductionView.as_view(), name="html_introduction"),
    path('html/structure', HtmlStructureView.as_view(), name="html_structure"),
    path("html/text_formating", HtmlTextFormatingView.as_view(), name="html_textformating")
    
]