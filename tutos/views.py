from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
class IndexView(LoginRequiredMixin, View):
    template_name = "tuto.html"
    def get(self, request):
        return render(request, self.template_name)
class HtmlTutoView(LoginRequiredMixin, View):
    template_name = "htmltuto.html"
    def get(self, request):
        return render(request, self.template_name)
class HtmlIntroductionView(LoginRequiredMixin, View):
    template_name = "htmlIntroduction.html"
    def get(self, request):
        return render(request, self.template_name)
class HtmlDescriptionView(LoginRequiredMixin, View):
    template_name = "htmlDescription.html"
    def get(self, request):
        return render(request, self.template)
class VSCodeTutoView(LoginRequiredMixin, View):
    template_name = "vscodetuto.html"
    def get(self, request):
        return render(request, self.template_name)
# Create your views here.
