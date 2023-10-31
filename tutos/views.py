from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, View):
    template_name = "tuto_index.html"
    def get(self, request):
        return render(request, self.template_name)

# Create your views here.
