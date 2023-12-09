from django.urls import path
from .views import *

app_name = "cart_check"
urlpatterns = [
    path('cart/',CartView.as_view(), name="cart"),
    # path('checkout/',CheckView.as_view(), name="cart"),
    path('',CartView.as_view(), name="cart"),
    path('',CartView.as_view(), name="cart"),
    
]
