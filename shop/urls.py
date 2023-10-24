from django.contrib import admin
from django.urls import path
from .views import *

app_name = "shop"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('about/',AboutView.as_view(),name='about'),
    path('service/',ServiceView.as_view(),name='service'),
    path('sales/',SalesView.as_view(),name='sales'),
    path('contact/',ContactView.as_view(),name='contact'),
    path("test/", TestView.as_view(), name="test"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
