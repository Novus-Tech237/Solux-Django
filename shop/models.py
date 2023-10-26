from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.hashers import make_password

# class Product(models.Model):
#     prod_name = models.CharField(max_length=100)
#     prod_price = models.CharField(max_length=10)
#     image = models.ImageField(upload_to='products')
#     description = models.TextField()
#     def __str__(self):
#         return self.prod_name
# class Cart(models.Model):
#     cart_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
#     completed = models.BooleanField(default=False)
#     def __str__(self):
#         return str(self.cart_id)
# class CartProduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item')
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
#     quantity = models.IntegerField(default=0)
#     def __str__(self):
#         return self.product.prod_name
class PDF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    forget_password_token = models.CharField(max_length=100, null=True, blank=True)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    def __str__(self):
        return self.user.username + 'Profile'