from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
    # Add more fields as needed, such as category, image, etc.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_name = models.CharField(max_length=100)  # Add order name field
    # Add more fields as needed, such as total amount, status, delivery address, etc.
