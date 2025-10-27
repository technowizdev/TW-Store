from django.db import models
from products.models import Product

class Lead(models.Model):
    STATUS_CHOICES = [('new','New'), ('contacted','Contacted'), ('completed','Completed')]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product.title if self.product else 'No Product'}"
