from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string

class CartView(LoginRequiredMixin, View):
    template_name = "cart.html"
    def get(self, request):
        return render(request, self.template_name)
# Create your views here.
